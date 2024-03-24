Summary: A virtual Ethernet switch system
Name: vde2
Version: 0
License: GPLv2 AND LGPL-2.1
URL: https://github.com/virtualsquare/vde-2

# git ls-remote https://github.com/virtualsquare/vde-2 HEAD
%global commit0 840a3e5db5fa79a95b9aae9b2f82d94194591f80
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/virtualsquare/vde-2/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz

Release: 1.20240323git.%shortcommit0%{?dist}

BuildRequires: libpcap-devel kernel-headers autoconf
Requires: libpcap kernel-modules-core

%description
One of VDE's core concepts is a plug. 86Box, for example, allows for
plugging an emulated machine into a virtual switch created by VDE;
this virtual layer 2 switch is capable of carrying any Ethernet-based
protocols such as IP and IPX.

%prep
%setup -q -n vde-2-%commit0
autoreconf --install

%build
%configure --disable-cryptcab
make -j`nproc`

%install
make install DESTDIR=%buildroot

%files
%_sysconfdir/*
%_bindir/*
%_datadir/*
%_libdir/*
%_libexecdir/*
%_includedir/*
