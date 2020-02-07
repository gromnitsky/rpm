Summary: Lossy jpeg images optimization
Name: imgmin
Version: 0
License: MIT
URL: https://github.com/rflynn/imgmin

# https://fedoraproject.org/wiki/Packaging:SourceURL
%global commit0 3451031f89a7758048f1e136d14b9024f750e398
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/rflynn/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Release: 2.20161211git.%shortcommit0%{?dist}

BuildRequires: autoconf
Requires: ImageMagick-libs

%description
An automated method for generating optimally-sized JPEG images.

%prep
%setup -q -n %{name}-%{commit0}

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/*
