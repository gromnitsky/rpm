Name: ubuntumono-fonts
Summary: A monospace/fixed-width companion for The Ubuntu font family
Version: 1.002
Release: 1%{?dist}
License: UBUNTU FONT LICENCE Version 1.0
URL: https://github.com/canonical/UbuntuMono-fonts
Source0: https://github.com/canonical/UbuntuMono-fonts/releases/download/v1.002/UbuntuMono-fonts-%version.zip

BuildArch: noarch
BuildRequires: fontpackages-devel mkfontscale

%description
# empty

%prep
%setup -q -n UbuntuMono-fonts-%version

%build
cd ttf
mkfontscale
mkfontdir

%global	_fontpath %_sysconfdir/X11/fontpath.d

%install
install -d -m755 %buildroot/%_fontdir
install -p -m644 ttf/* %buildroot/%_fontdir

install -m755 -d %buildroot/%_fontpath
ln -s %_fontdir %buildroot/%_fontpath/%name

%files
%doc LICENCE.txt LICENCE-FAQ.txt
%_fontdir/*
%_fontpath/*
