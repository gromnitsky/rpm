Name: perfectspot
Version: 0.2.0
Release: 1%{?dist}
Summary: A graphical viewer for WordPerfect Graphics (WPG) files

License: GPLv2
URL: http://libwpg.sourceforge.net/perfectspot.htm
Source0: http://downloads.sourceforge.net/libwpg/%{name}-%{version}.tar.gz

BuildRequires: libwpg-devel qt-devel libodfgen-devel

%description
Supports vector & raster WPG variants, export to svg/pdf/jpg/odg/bmp.

%prep
%autosetup

%build
%cmake .
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
