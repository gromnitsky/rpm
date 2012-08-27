# Pass --without-x to rpmbuild to compile only vmtoolsd plugins that
# doesn't depend on X11.
%bcond_without x

%define upstream_name open-vm-tools
%define upstream_date 2012.05.21
%define upstream_rel 724730
Version: %{upstream_date}+%{upstream_rel}
Release: 1%{?dist}

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
BuildRequires: glib2-devel
Requires: glib2 pkgconfig
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

FAQ: https://github.com/gromnitsky/open-vm-tools-min-fedora

%prep
%setup -q -n %{upstream_name}-%{upstream_date}-%{upstream_rel}
%patch01
#patch02
%patch03
%patch04
%patch05

%build
%configure \
	%{?_without_x} \
	--without-icu --without-dnet --without-procps --without-pam \
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
echo *****************************************************
echo To copy/paste between host & guest, add to ~/.xinitrc
echo
echo vmtoolsd -n vmusr &
echo *****************************************************
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
