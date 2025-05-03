%global tcl_version 8.6
%global tcl_sitelib %{_datadir}/tcl%{tcl_version}

Summary: Tcl GUI console
Name: tkcon
Version: 2.7
License: TCL
URL: http://tkcon.sourceforge.net/

# $ cvs -z3 -d:pserver:anonymous@tkcon.cvs.sourceforge.net:/cvsroot/tkcon checkout tkcon
# $ tar cfz tkcon-`date +%F-%s`.tar.gz tkcon && rm -rf tkcon
Source0: %{name}-2017-08-19-1503123300.tar.gz

patch1: wish.patch

Release: 2.20170819cvs.1503123300%{?dist}

BuildArch: noarch
BuildRequires: desktop-file-utils, tcllib
Requires: tk8, perl-Tk

%description
tkcon is a replacement for the standard Tk console with many more features.
It works on all platforms where Tcl/Tk is available.
It is meant primarily to aid one when working with the little details
inside tcl and tk, giving Unix users the GUI console provided by default
in the Mac and Windows Tk.

%prep
%setup -q -n %{name}
%patch -P 1 -p0 -b .wish
mkdir man
mv docs/*.man man

# observe.n man page conflicts w/ tcllib's tcl::transform::observe module;
# rename observe(n) refs to tkcon_observe(n) in all the relevant man pages
sed -i'' 's/\[cmd observe](n)/[cmd tkcon_observe](n)/' `ls man/*.man | grep -v observe`
mv man/observe.n.man man/tkcon_observe.n.man

rm -rf docs/CVS docs/changes.txt
chmod 644 docs/*
sed -i'' s,/usr/local/bin/perl,/usr/bin/perl, docs/perl.txt

%build
# man pages
for idx in man/*; do
    dtplite -o ${idx%.*} nroff $idx
done

%install
%define my_libdir %{tcl_sitelib}/%{name}-%{version}
# to test the package, run
# $ echo 'puts [package require tkcon]; exit' | tclsh
install -D -m644 tkcon.tcl $RPM_BUILD_ROOT/%{my_libdir}/tkcon.tcl
install -D -m644 pkgIndex.tcl $RPM_BUILD_ROOT/%{my_libdir}/pkgIndex.tcl

install -D tkcon.tcl $RPM_BUILD_ROOT/%{_bindir}/tkcon

desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications --set-icon=tkcon tkcon-console.desktop
install -D -m644 icons/tkcon-small.svg $RPM_BUILD_ROOT/%{_datadir}/pixmaps/tkcon.svg

# man pages
install -D -m644 man/*.1 -t ${RPM_BUILD_ROOT}%{_mandir}/man1
install -D -m644 man/*.5 -t ${RPM_BUILD_ROOT}%{_mandir}/man5
install -D -m644 man/*.n -t ${RPM_BUILD_ROOT}%{_mandir}/mann

%files
%{_bindir}/*
%{my_libdir}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/*/*
%doc docs/* ChangeLog
