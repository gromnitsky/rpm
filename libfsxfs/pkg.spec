Name: libfsxfs
Version: 20231124
Release: 1
Summary: Library to support the X File System (XFS) format
License: LGPL-3.0-or-later
Source: https://github.com/libyal/%name/releases/download/%version/%name-experimental-%version.tar.gz
URL: https://github.com/libyal/libfsxfs

BuildRequires: fuse-devel openssl-devel

%description
Several tools for reading X File System (XFS) volumes

%prep
%setup -q

%build
%configure --disable-nls --enable-wide-character-type
%make_build

%install
%make_install

%files
%_bindir/*
%_includedir/*
%_libdir/*
%_datadir/*
