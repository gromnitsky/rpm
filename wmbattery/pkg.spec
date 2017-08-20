Summary: Dockapp for laptop ACPI information
Name: wmbattery
Version: 2.50
Release: 1
License: GPL2
Group: User Interface/X

URL: http://www.dockapps.net/wmbattery
Source0: http://www.dockapps.net/download/%{name}-%{version}.tar.gz

BuildRequires: libXpm-devel

%description
wmbattery displays the status of your laptop's battery in a small icon. This
includes if it is plugged in, if the battery is charging, how many minutes
of battery life remain, battery life remaining (with both a percentage and a
graph), and battery status (high - green, low - yellow, or critical - red).

%prep
%setup -q -n dockapps-30b9edb

%build
make prefix=%{_prefix}

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/icons/*
%{_mandir}/*/*
