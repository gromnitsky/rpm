# This doesn't install mozjpeg for it conflicts w/ Fedora
# libjpeg-turbo-devel package! We compile mozjpeg solely for the
# purpose of the jpeg-archive build process. The resulting
# jpeg-archive binaries don't depend upon mozjpeg.

Summary: CLI utilities for archiving photos
Name: jpeg-archive
Version: 2.2.0
License: MIT
URL: https://github.com/danielgtaylor/jpeg-archive

# https://fedoraproject.org/wiki/Packaging:SourceURL
%global commit0 397fa1e9ed688d919e5257c47a31ef69dffa8baf
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/danielgtaylor/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Release: 1.20191228git.%shortcommit0%{?dist}

%global commit1 bbb7550709d396aae66d5ea5fad5ef06b1ec7f59
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
Source1: https://github.com/mozilla/mozjpeg/archive/%{commit1}.tar.gz#/mozjpeg-%{shortcommit1}.tar.gz

BuildRequires: cmake, nasm
Requires: parallel, dcraw, perl-Image-ExifTool

%description
jpeg-archive, jpeg-compare, jpeg-hash, jpeg-recompress.
Uses MozJPEG encoder.

%prep
rm -rf mozjpeg-%commit1 mozjpeg mozjpeg-build
tar xfz $RPM_SOURCE_DIR/mozjpeg-%shortcommit1.tar.gz
mkdir mozjpeg-build && cd mozjpeg-build
cmake -G"Unix Makefiles" -DWITH_JPEG8=1 -DPNG_SUPPORTED=0 \
      -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_DIR/mozjpeg ../mozjpeg-%commit1
make install

cd $RPM_BUILD_DIR
rm -rf %name-%commit0
tar xfz $RPM_SOURCE_DIR/%name-%shortcommit0.tar.gz

%build
cd $RPM_BUILD_DIR/%name-%commit0
%make_build MOZJPEG_PREFIX=$RPM_BUILD_DIR/mozjpeg

%install
cd $RPM_BUILD_DIR/%name-%commit0
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%defattr(-,root,root,-)
%{_bindir}/*
