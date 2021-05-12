Summary: A DEC SIXEL graphics encoder/decoder and converter programs
Name: libsixel
Version: 0
License: MIT
URL: https://github.com/saitoha/libsixel

# git ls-remote https://github.com/saitoha/libsixel HEAD
%global commit0 6a5be8b72d84037b83a5ea838e17bcf372ab1d5f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/saitoha/%name/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz

Release: 1.20210512git.%shortcommit0%{?dist}

Requires: libpng libjpeg-turbo
BuildRequires: libpng-devel libjpeg-turbo-devel

%description
SIXEL is one of image formats for printer and terminal imaging
introduced by Digital Equipment Corp. (DEC). Its data scheme is
represented as a terminal-friendly escape sequence. So if you want to
view a SIXEL image file, all you have to do is "cat" it to your
terminal.

%prep
%setup -q -n %name-%commit0

%build
%configure --disable-python --with-libcurl=no
%make_build

%install
%make_install

%files
%_bindir/*
%_includedir/*
%_libdir/*
%_datadir/*
