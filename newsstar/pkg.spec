Name: newsstar
Version: 1.5.6
Release: 1%{?dist}
Summary: Fetches news and posts it to a local NNTP server

License: GPLv3
URL: http://%{name}.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: inn, gdbm-devel, ncurses-devel, openssl-devel, xmlto
Requires: inn

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

%prep
%setup -q


%build
%configure \
	--enable-keyed-log \
	--with-inn-path=%{_libexecdir}/news \
	--with-outgoing-dir=%{dir_outgoing} \
	--disable-chown
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{dir_conf} $RPM_BUILD_ROOT%{dir_rc} \
	$RPM_BUILD_ROOT%{dir_incoming}

cp -a sample_config $RPM_BUILD_ROOT%{_docdir}/%{name}

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


%changelog
