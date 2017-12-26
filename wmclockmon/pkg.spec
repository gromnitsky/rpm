Summary: A nice digital clock with 7 different LCD/LED styles
Name: wmclockmon
Version: 0.8.1
Release: 1%{?dist}
License: GPLv2

URL: http://tnemeth.free.fr/projets/dockapps.html
Source0: http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz

BuildRequires: gtk2-devel
Requires: gtk2

# https://aur.archlinux.org/cgit/aur.git/tree/build2.0.patch?h=wmclockmon
patch0: gtk2.patch

%description
A nice digital clock with 7 different styles either in LCD style and
LED style, and that uses locales to display week-day and month names.

%prep
%setup -q
%patch0 -p2 -b .orig
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install
install -D -m644 doc/sample* -t ${RPM_BUILD_ROOT}%{_docdir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}/*
%{_docdir}/%{name}/*
