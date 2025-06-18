Name: 86Box
Version: 0
Summary: Emulator of x86-based machines
License: GPLv2

# https://fedoraproject.org/wiki/Packaging:SourceURL
# git ls-remote https://github.com/86Box/86Box
%global commit0 dd305a174cc70f7b21c0d6e2f07c03422635f2e1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/%name/%name/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Release: 1.20250618git.%shortcommit0%{?dist}

%global roms 4.2.1
Source1: https://github.com/86Box/roms/archive/refs/tags/v%{roms}.tar.gz

URL: https://github.com/86Box/86Box

BuildRequires: cmake extra-cmake-modules pkg-config ninja-build freetype-devel SDL2-devel libatomic libpng-devel libslirp-devel libXi-devel openal-soft-devel rtmidi-devel fluidsynth-devel libsndfile-devel libserialport-devel qt5-linguist qt5-qtconfiguration-devel qt5-qtbase-private-devel qt5-qtbase-static wayland-devel libevdev-devel libxkbcommon-x11-devel zlib-ng-compat-static


%description
86Box is a low level x86 emulator that runs older operating systems
and software designed for IBM PC systems and compatibles from 1981
through fairly recent system designs based on the PCI bus.

%prep
%setup -q -c
%setup -q -D -T -a 1

%build
# undo '-Werror=format-security' from /usr/lib/rpm/redhat/macros
%global _warning_options -Wall

cd %name-%commit0
cmake -B _out -S . --preset optimized
cmake --build _out

%install
cd %name-%commit0
cmake --install _out --prefix %{buildroot}%{_prefix}
cd ../roms-%{roms}
mkdir -p %buildroot/%_datadir/86Box/roms
cp -r . %buildroot/%_datadir/86Box/roms

%files
%_bindir/*
%_datadir/*
