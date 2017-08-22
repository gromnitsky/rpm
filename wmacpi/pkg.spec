Summary: A dockapp ACPI battery monitor
Name: wmacpi
Version: 2.3
Release: 1%{?dist}
License: GPL2

URL: http://www.dockapps.net/wmacpi
Source0: http://www.dockapps.net/download/wmacpi-%{version}.tar.gz

BuildRequires: libdockapp-devel

patch0: wmacpi.1.patch

%description
wmacpi is a dockapp ACPI battery monitor. It opens various files under
/proc/acpi, reads status information from them, and then displays
summaries. It provides full support for multiple batteries.

If it draws a black window, try to start it as 'wmacpi -w'.

%prep
%setup -q -n dockapps
%patch0 -b .orig

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*/*
%doc README
