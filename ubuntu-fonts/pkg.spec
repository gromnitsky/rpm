Name: ubuntu-fonts
Summary: The Ubuntu font family
Version: 1.001
Release: 1%{?dist}
License: UBUNTU FONT LICENCE Version 1.0
URL: https://github.com/canonical/Ubuntu-fonts
Source0: https://github.com/canonical/Ubuntu-fonts/releases/download/v.1001/Ubuntu-fonts-%version.zip

BuildArch: noarch
BuildRequires: fontpackages-devel mkfontscale

%description
# empty

%prep
%setup -q -n Ubuntu-fonts-%version

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
