# Pass --without=x to rpmbuild to compile only vmtoolsd plugins that
# doesn't depend on X11.
%bcond_without x

%define upstream_name open-vm-tools
%define upstream_date 2013.04.16
%define upstream_rel 1098359
Version: %{upstream_date}+%{upstream_rel}
Release: 2%{?dist}

%if %{without x}
Name: %{upstream_name}-min-fedora-nox11
%else
Name: %{upstream_name}-min-fedora
%endif

Summary: Open VMware tools for VMware guests (a light version)
Group: Applications/System
# GPLv2 kernel modules are not included anyway
License: LGPLv2.1 and BSD
URL: http://%{upstream_name}.sourceforge.net/
# Starting Fedora 19 there is an package in their official repo. But we
# don't like that package!
Conflicts: %{upstream_name}

Source0: http://downloads.sourceforge.net/%{upstream_name}/%{upstream_name}-%{upstream_date}-%{upstream_rel}.tar.gz
%define systemd_service %{upstream_name}-min.service
Source1: %{systemd_service}

patch01: patch-Makefile.in
#patch02: patch-scripts-Makefile.in
patch03: patch-services-plugins-Makefile.in
patch04: patch-services-vmtoolsd-Makefile.in
patch05: patch-toolbox-Makefile.in

AutoReq: no

%if %{without x}
BuildRequires: glib2-devel, procps-devel, libdnet-devel
Requires: glib2, pkgconfig, procps, libdnet
%else
BuildRequires: libXinerama-devel, libSM-devel, libXrandr-devel, libXtst-devel
BuildRequires: gtkmm24-devel
Requires: libXinerama, libSM, libXrandr, libXtst
Requires: gtkmm24
%endif

%description
The %{upstream_name} are a subset of the VMware Tools, currently
composed of user-space programs for Fedora 17+ guest operating systems.

This RPM does not contain kernel & fuse modules.
Unity support is disabled by upstream.

%prep
%setup -q -n %{upstream_name}-%{upstream_date}-%{upstream_rel}
%patch01
#patch02
%patch03
%patch04
%patch05

%build
# Use -Wno-unused-local-typedefs to build with GCC 4.8
export CFLAGS="$RPM_OPT_FLAGS -Wno-unused-local-typedefs"
export CXXLAGS="$RPM_OPT_FLAGS -Wno-unused-local-typedefs"
%configure \
	%{?_without_x} \
	--without-icu --without-pam \
	--without-kernel-modules --disable-docs --disable-tests
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# systemd
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}


%files
%{_bindir}/*
%{_sysconfdir}/*
%{_includedir}/*
%{_libdir}/lib*
%{_libdir}/%{upstream_name}/*
%{_libdir}/pkgconfig/*

%{_unitdir}/%{systemd_service}


%post
if [ "$1" = 1 ]; then
	%{_bindir}/vmware-toolbox-cmd timesync enable
	systemctl enable %{systemd_service}
	systemctl start %{systemd_service}
fi
%if ! %{without x}
echo '*****************************************************'
echo 'To copy/paste between host & guest, add to ~/.xinitrc'
echo ''
echo 'vmtoolsd -n vmusr &'
echo '*****************************************************'
%endif

%preun
if [ "$1" = 0 ]; then
	systemctl --no-reload disable %{systemd_service} || :
	systemctl stop %{systemd_service}
fi
exit 0

%postun
systemctl daemon-reload


%changelog
