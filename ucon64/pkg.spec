Summary: A Swiss Army knife of video game emulators
Name: ucon64
Version: 2.1.0
%global rev 2706
Release: %rev.1%{?dist}
License: GPLv2+
URL: http://ucon64.sourceforge.net

# u=svn://svn.code.sf.net/p/ucon64/svn/trunk/ucon64/
# svn export $u ucon64-`svn info --show-item revision $u`
# tar cfJ ucon64-2706.tar.xz ucon64-2706 && rm -rf ucon64-2706
Source0: ucon64-%rev.tar.xz

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
%defattr(-,root,root,-)
%_bindir/*
%_libdir/*
%doc images changes.html developers.html faq.html hardware.html
