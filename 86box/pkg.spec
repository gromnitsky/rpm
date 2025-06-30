Name: 86Box
Version: 0
Summary: Emulator of x86-based machines
License: GPLv2
URL: https://github.com/86Box/86Box

%global forgeurl0 https://github.com/86Box/86Box
# git ls-remote https://github.com/86Box/86Box master
%global commit0 7d579fb3f994bfb98c186902803e5787aabe5761

%global forgeurl1 https://github.com/86Box/roms
# git ls-remote https://github.com/86Box/roms master
%global commit1 2f32824f0d116f74ac4b553492d2689b305e6220

%forgemeta -a
Source0: %{forgesource0}
Source1: %{forgesource1}
Release: 1%{?dist}

BuildRequires: cmake extra-cmake-modules pkg-config ninja-build freetype-devel SDL2-devel libatomic libpng-devel libslirp-devel libXi-devel openal-soft-devel rtmidi-devel fluidsynth-devel libsndfile-devel libserialport-devel qt5-linguist qt5-qtconfiguration-devel qt5-qtbase-private-devel qt5-qtbase-static wayland-devel libevdev-devel libxkbcommon-x11-devel zlib-ng-compat-static

%description
86Box is a low level x86 emulator that runs older operating systems
and software designed for IBM PC systems and compatibles from 1981
through fairly recent system designs based on the PCI bus.


%prep
%forgesetup -a

%build
# undo '-Werror=format-security' from /usr/lib/rpm/redhat/macros
%global _warning_options -Wall

cd ../%name-%commit0
cmake -B _out -S . --preset optimized
cmake --build _out

%install
cd ../%name-%commit0
cmake --install _out --prefix %{buildroot}%{_prefix}
cd ../roms-%commit1
mkdir -p %buildroot/%_datadir/86Box/roms
cp -r . %buildroot/%_datadir/86Box/roms

%files
%_bindir/*
%_datadir/*
