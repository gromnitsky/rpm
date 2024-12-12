Summary: A Swiss Army knife of video game emulators
Name: ucon64
Version: 0
%global rev 2933
Release: 1.20231121svn.%rev%{?dist}
License: GPLv2+
URL: https://ucon64.sourceforge.net

# svn info https://svn.code.sf.net/p/ucon64/svn/ | grep Revision
# svn export -r $rev svn://svn.code.sf.net/p/ucon64/svn/trunk/ucon64 ucon64-$rev
# tar cfJ ucon64-$rev.tar.xz ucon64-$rev && rm -rf ucon64-$rev
Source0: %name-%rev.tar.xz

BuildRequires: zlib-devel libusb-compat-0.1-devel
Requires: zlib libusb-compat-0.1

Patch1: discmage.patch

%description

%prep
%setup -q -n %name-%rev

%patch 1 -p0 -b .discmage
sed -i 's|@@_libdir@@|%_libdir|' src/ucon64_misc.c

%build
cd src
%configure --with-libusb --with-libdiscmage
export CFLAGS="$CFLAGS -Wno-error=format-security"
%make_build

%install
install -D src/ucon64 -t $RPM_BUILD_ROOT/%_bindir
install -D src/libdiscmage/discmage.so $RPM_BUILD_ROOT/%_libdir/libdiscmage.so

%files
%_bindir/*
%_libdir/*
%doc images changes.html developers.html faq.html hardware.html
