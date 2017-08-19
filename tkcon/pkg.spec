Summary: Tcl GUI console
Name: tkcon
Version: 2.7
Release: 0.1.pre1%{?dist}
License: TCL
Group: Development/Tools
URL: http://tkcon.sourceforge.net/

# $ cvs -z3 -d:pserver:anonymous@tkcon.cvs.sourceforge.net:/cvsroot/tkcon checkout tkcon
# $ tar cfz tkcon-`date +%F-%s`.tar.gz tkcon && rm -rf tkcon
Source0: %{name}-2017-08-19-1503123300.tar.gz

BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: tk, perl-Tk

%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %define tcl_sitelib %{_datadir}/tcl%{tcl_version}}

%description
tkcon is a replacement for the standard Tk console with many more features.
It works on all platforms where Tcl/Tk is available.
It is meant primarily to aid one when working with the little details
inside tcl and tk, giving Unix users the GUI console provided by default
in the Mac and Windows Tk.

%prep
%setup -q -n %{name}
rm -rf docs/*.man docs/CVS
chmod 644 docs/*
sed -i'' s,/usr/local/bin/perl,/usr/bin/perl, docs/perl.txt

%install
install -pD tkcon.tcl $RPM_BUILD_ROOT/%{_bindir}/tkcon

# to test the package, run
# $ echo 'puts [package require tkcon]; exit' | tclsh
install -pD -m644 tkcon.tcl $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}-%{version}/tkcon.tcl
install -pD -m644 pkgIndex.tcl $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}-%{version}/pkgIndex.tcl

desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications --set-icon=tkcon tkcon-console.desktop
mkdir $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
install -p -m644 icons/tkcon-small.svg $RPM_BUILD_ROOT/%{_datadir}/pixmaps/tkcon.svg

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{tcl_sitelib}/%{name}-%{version}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%doc docs/* ChangeLog

%changelog

