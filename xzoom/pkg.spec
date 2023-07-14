Name: xzoom
Version: 0.4
Release: 1%{?dist}
Summary: Magnify part of the screen, with fast updates
License: MIT
Source0: http://www.linklevel.net/distfiles/%{name}-%{version}.tar.gz

BuildRequires: libX11, imake

%description
Xzoom displays in its window a magnified area of the X11 display. The
user can interactively change the zoomed area, the window size,
magnification (optionally different magnification for X and Y axes) or
rotate or mirror the image.

%prep
%setup -q

%build
xmkmf
make %{?_smp_mflags}

%install
install -p xzoom -D -t $RPM_BUILD_ROOT%{_bindir}
install -m 644 -p xzoom.man -D -T $RPM_BUILD_ROOT%{_mandir}/man1/xzoom.1

%files
%{_bindir}/*
%{_mandir}/*
