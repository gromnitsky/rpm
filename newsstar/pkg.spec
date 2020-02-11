Name: newsstar
Version: 1.5.6
Release: 3%{?dist}
Summary: Fetches news and posts it to a local NNTP server

License: GPLv3
URL: http://%{name}.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: inn, gdbm-devel, ncurses-devel, xmlto
Requires: inn, compat-openssl10

%description
What makes newsstar special is that it can make multiple simultaneous
connections, not only to one server, but to several, supporting up to 10
threads. Before fetching each article it checks that it has not already
been downloaded by another thread or in a previous session. It can also
pipeline article requests to make better use of available bandwidth.

# http://newsstar.sourceforge.net/ar01s05.html
%define dir_conf %{_sysconfdir}/%{name}
%define dir_rc %{_sharedstatedir}/%{name}
%define dir_incoming %{_localstatedir}/spool/%{name}-incoming

%define dir_outgoing %{_localstatedir}/spool/news/outgoing
#%define dir_articles %{_localstatedir}/spool/news/articles

%global openssl %{_builddir}/openssl10

%prep
# download & unpack openssl 1.0x
mkdir %{openssl} && pushd %{openssl}
[ -f compat-openssl10-1.*.rpm -a -f compat-openssl10-devel-1.*.rpm ] || {
  dnf download compat-openssl10.%{_arch} compat-openssl10-devel.%{_arch}
  rpm2cpio compat-openssl10-1.*.rpm | cpio -idm
  rpm2cpio compat-openssl10-devel-1.*.rpm | cpio -idm
}
%setup -q


%build
export CFLAGS='-I%{openssl}/usr/include'
export LDFLAGS='-L%{openssl}/usr/%{_lib}'
%configure \
	--enable-keyed-log \
	--with-inn-path=%{_libexecdir}/news \
	--with-outgoing-dir=%{dir_outgoing} \
	--disable-chown --enable-ssl
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{dir_conf} $RPM_BUILD_ROOT%{dir_rc} \
	$RPM_BUILD_ROOT%{dir_incoming}

cp -a sample_config $RPM_BUILD_ROOT%{_docdir}/%{name}
rm %{openssl}/*.rpm

%files
%{_bindir}/*
%{_libexecdir}/%{name}/*
%{_docdir}/*
%{_mandir}/*
%{dir_conf}
%{dir_rc}
%{dir_incoming}

%post
chown news:news %{_bindir}/%{name} \
	%{_libexecdir}/%{name}/%{name}.bin
chown -R news:news %{dir_conf} %{dir_rc} %{dir_incoming}
