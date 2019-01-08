Summary: A Swiss Army knife of video game emulators
Name: ucon64
Version: 2.1.0
%global rev 2706
Release: 1.20190104svn.%rev%{?dist}
License: GPLv2+
URL: http://ucon64.sourceforge.net

# svn export -r $rev svn://svn.code.sf.net/p/ucon64/svn/trunk/ucon64 ucon64-$rev
# tar cfJ ucon64-$rev.tar.xz ucon64-$rev && rm -rf ucon64-$rev
Source0: %name-%rev.tar.xz

Patch1: discmage.patch

%description

%prep
%setup -q -n %name-%rev

%patch1 -p0 -b .discmage
sed -i 's|@@_libdir@@|%_libdir|' src/ucon64_misc.c

%build
cd src
%configure --with-libusb
export CFLAGS="$CFLAGS -Wno-error=format-security"
%make_build

%install
install -D src/ucon64 -t $RPM_BUILD_ROOT/%_bindir
install -D src/libdiscmage/discmage.so $RPM_BUILD_ROOT/%_libdir/libdiscmage.so

%files
%_bindir/*
%_libdir/*
%doc images changes.html developers.html faq.html hardware.html
