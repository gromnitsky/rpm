Name: libdvdcss
Version: 1.4.3
Release: 1%{?dist}
Summary: A library designed for accessing DVDs like a block device without having to bother about the decryption
License: GPLv2+
URL: https://www.videolan.org/developers/libdvdcss.html
Source0: https://download.videolan.org/pub/videolan/%name/%version/%name-%version.tar.bz2
BuildRequires:  gcc, make

%description
A DVD player can be built around the libdvdcss API using no more than
4 or 5 library calls. Unlike most similar projects, libdvdcss does not
require the region of your drive to be set.

%package devel
Summary: Development files for libdvdcss
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development files for libdvdcss.

%prep
%setup -q

%build
%configure
make V=1 %{?_smp_mflags}

%install
%make_install
%ldconfig_scriptlets

%files
%{_libdir}/libdvdcss.so.2*

%files devel
%{_datarootdir}/doc/*
%{_includedir}/dvdcss
%{_libdir}/libdvdcss.so
%{_libdir}/libdvdcss.a
%{_libdir}/pkgconfig/libdvdcss.pc
