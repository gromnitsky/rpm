Name: xmem
Version: 1.20
Release: 1%{?dist}
Summary: Memory/swap usage display utility for X
License: MIT

Source0: %{name}_%{version}-27.tar.gz

Patch0: Makefile.patch

BuildRequires: libXext-devel libXpm-devel libXt-devel libXmu-devel procps-ng-devel libXaw-devel

%description
The XMEM program displays the used amount of memory/swap.

How to use it: http://www.xteddy.org/xmem.html

%prep
%setup -n %name-%version
%patch0 -p0

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m644 xmem.1x $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/X11/app-defaults/*
%config(noreplace) %{_datadir}/X11/app-defaults/*
