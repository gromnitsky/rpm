Summary: Module to create vector screenshots of GTK3-based programs
Name: gtk-vector-screenshot
Version: 0
License: GPLv2+
URL: https://github.com/nomeata/gtk-vector-screenshot

# git ls-remote https://github.com/nomeata/gtk-vector-screenshot HEAD
%global commit0 af9cae0f2010a9c1451fc36516e1f1dfb226db1a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/nomeata/%name/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz

patch1: destroy.patch

Release: 1.20241211git.%shortcommit0%{?dist}

BuildRequires: gtk3-devel

%description
This gtk module allows you to take a screenshot of a running gtk-3 application
as a vector image, with fully scalable graphics and selectable text. It
supports rendering the application to PDF, SVG and PostScript.

%prep
%setup -q -n %name-%commit0
%patch -P 1 -p0 -b .orig

%build
libtoolize
aclocal
autoheader
automake --add-missing
autoconf
%configure
%make_build

%install
%make_install
install -D -m644 52load-gtk-vector-screenshot-gtk-module -t $RPM_BUILD_ROOT/etc/X11/Xsession.d

%files
%_bindir/*
%_libdir/*
%_datadir/*
%_sysconfdir/*
