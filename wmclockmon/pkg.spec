Summary: A nice digital clock with 7 different LCD/LED styles
Name: wmclockmon
Version: 0.8.1
Release: 2%{?dist}
License: GPLv2

URL: http://tnemeth.free.fr/projets/dockapps.html
Source0: http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz

BuildRequires: gtk2-devel
Requires: gtk2

patch2: update_autotools.patch
patch3: build_against_gtk2.patch
patch4: fix_typos.patch
patch5: check_free.patch
patch6: add_extern.patch
patch7: fix_leaks.patch

%description
A nice digital clock with 7 different styles either in LCD style and
LED style, and that uses locales to display week-day and month names.

%prep
%setup -q
%patch -P 2 -p1 -b .orig
%patch -P 3 -p1 -b .orig
%patch -P 4 -p1 -b .orig
%patch -P 5 -p1 -b .orig
%patch -P 6 -p1 -b .orig
%patch -P 7 -p1 -b .orig
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install
install -D -m644 doc/sample* -t ${RPM_BUILD_ROOT}%{_docdir}/%{name}
find styles -type f | grep -v Makefile | xargs install -D -m644 -t ${RPM_BUILD_ROOT}%{_datadir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}/*
%{_docdir}/%{name}/*
