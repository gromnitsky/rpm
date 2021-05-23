Name: daewoo-misc-fonts
Version: 1.0.3
Release: 1%{?dist}
Summary: X.Org miscellaneous Daewoo fonts

License: Unknown
Source: https://www.x.org/releases/individual/font/font-daewoo-misc-%version.tar.gz

BuildArch: noarch
BuildRequires: bdftopcf mkfontscale
%dnl %_fontdir macro
BuildRequires: fontpackages-devel

%description
This are the PCF versions of the Daewoo Gothic fonts for 100dpi displays.

%prep
%setup -q -n font-daewoo-misc-%version

%build
for file in *.bdf; do
    bdftopcf -t "$file" | gzip > "${file%.*}".pcf.gz
done


%global	_fontpath %_sysconfdir/X11/fontpath.d

%install
install -D -m644 *.pcf.gz -t $RPM_BUILD_ROOT/%_fontdir
mkfontdir $RPM_BUILD_ROOT/%_fontdir

install -m755 -d $RPM_BUILD_ROOT/%_fontpath
ln -s %_fontdir $RPM_BUILD_ROOT/%_fontpath/%name


%files
%_fontdir
%_fontpath/*
