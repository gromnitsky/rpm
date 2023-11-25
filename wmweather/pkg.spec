Name: wmweather
Version: 2.4.7
Release: 1%{?dist}
Summary: A dockapp weather applet
License: GPLv2+

URL: https://people.debian.org/~godisch/wmweather/
Source0: https://people.debian.org/~godisch/wmweather/wmweather-%version.tar.gz
Patch0: gcc10.patch

BuildRequires: curl-devel libXext-devel libXpm-devel
Requires: xmessage xorg-x11-fonts-misc curl libXpm libXext

%description
wmWeather is a dockapp that displays
weather conditions using the METAR reports.

%prep
%setup -q
%patch 0 -p1 -b .gcc10

%build
cd src
%configure
make

%install
cd src
make install DESTDIR=%buildroot
rm %buildroot/%_bindir/wmWeather
rm %buildroot/%_datadir/*/*/wmWeather*

%files
%doc CHANGES README
%_bindir/*
%_datadir/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
