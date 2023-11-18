# This doesn't install mozjpeg for it conflicts w/ Fedora
# libjpeg-turbo-devel package! We compile mozjpeg solely for the
# purpose of the jpeg-archive build process. The resulting
# jpeg-archive binaries don't depend upon mozjpeg.

Summary: CLI utilities for archiving photos
Name: jpeg-archive
Version: 0
License: MIT
URL: https://github.com/danielgtaylor/jpeg-archive

# https://fedoraproject.org/wiki/Packaging:SourceURL
# git ls-remote https://github.com/danielgtaylor/jpeg-archive HEAD
%global commit0 5b56afa11872fc4b9f68c5a3dcf2ec5afe869504
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/danielgtaylor/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Release: 1.20231118git.%shortcommit0%{?dist}

# git ls-remote https://github.com/mozilla/mozjpeg HEAD
%global commit1 6c9f0897afa1c2738d7222a0a9ab49e8b536a267
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
Source1: https://github.com/mozilla/mozjpeg/archive/%{commit1}.tar.gz#/mozjpeg-%{shortcommit1}.tar.gz

BuildRequires: cmake, nasm, libpng-static
Requires: parallel, dcraw, perl-Image-ExifTool

%global mozjpeg $RPM_BUILD_DIR/%name-%version/mozjpeg-install

%description
jpeg-archive, jpeg-compare, jpeg-hash, jpeg-recompress.
Uses MozJPEG encoder.

%prep
# extract all the sources under an umbrella dir %name-%version
%setup -q -c
%setup -q -D -T -a 1

mkdir mozjpeg-build && cd mozjpeg-build
cmake -G"Unix Makefiles" -DCMAKE_INSTALL_PREFIX=%mozjpeg ../mozjpeg-%commit1
make install

%build
cd %name-%commit0
unset LDFLAGS
CFLAGS=-fcommon %make_build MOZJPEG_PREFIX=%mozjpeg

%install
cd %name-%commit0
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/*
