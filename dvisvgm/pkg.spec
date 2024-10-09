Summary: Convert DVI, EPS, PDF to SVG
Name: dvisvgm
Version: 0
License: GPLv3
URL: https://github.com/mgieseki/dvisvgm
Conflicts: texlive-dvisvgm

# git ls-remote https://github.com/mgieseki/dvisvgm HEAD
%global commit0 0ff668ed33bb2f57034fede8712e05bff2d9232e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/mgieseki/dvisvgm/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz

Release: 1.20241009git.%shortcommit0%{?dist}

BuildRequires: autoconf asciidoc xmlto mupdf-devel ttfautohint-devel texlive-lib-devel freetype-devel zlib-ng-compat-devel woff2-devel brotli-devel xxhash-devel potrace-devel
Requires: ttfautohint

%description
.

%prep
%setup -q -n dvisvgm-%commit0
autoreconf -fi

%build
%configure --with-ttfautohint
make -j`nproc`

%install
make install DESTDIR=%buildroot

%files
%_bindir/*
%_datadir/*
