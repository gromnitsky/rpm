Name: xlayoutdisplay
Version: 1.5.0
Release: 1%{?dist}
Summary: Detects (with XRandR) and arranges (with xrandr) display outputs
License: Apache-2.0
URL: https://github.com/alex-courtis/xlayoutdisplay

Source0: https://github.com/alex-courtis/xlayoutdisplay/archive/refs/tags/v%{version}.tar.gz
Requires: libXrandr
BuildRequires: libXrandr-devel

%description
.

%prep
%setup -q

%build
%make_build

%install
install -D -m755 xlayoutdisplay -t $RPM_BUILD_ROOT%{_bindir}
install -D -m644 .xlayoutdisplay 99-xlayoutdisplay.rules README.md -t ${RPM_BUILD_ROOT}%{_docdir}/%{name}

%files
%{_bindir}/*
%{_docdir}/*
