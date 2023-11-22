Name: xmem
Version: 1.20
Release: 2%{?dist}
Summary: Memory/swap usage display utility for X
License: MIT

Source0: %{name}_%{version}-27.tar.gz
Source1: https://downloads.sourceforge.net/procps-ng/procps-ng-3.3.17.tar.xz

Patch0: Makefile.patch

BuildRequires: libXext-devel libXpm-devel libXt-devel libXmu-devel libXaw-devel

%description
The XMEM program displays the used amount of memory/swap.

How to use it: http://www.xteddy.org/xmem.html

%prep
%setup -q -n %name-%version
%patch 0 -p0

cp %{SOURCE1} .
tar xf procps-ng-3.3.17.tar.xz
cd procps-3.3.17
./configure --prefix=`pwd`/1
make install

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m644 xmem.1x $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_datadir}/X11/app-defaults/*
