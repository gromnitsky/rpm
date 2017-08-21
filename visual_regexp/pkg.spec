Summary: Tk regexp visual designer
Name: visual_regexp
Version: 3.0.1
Release: 2%{?dist}
License: GPLv2+
URL: http://laurent.riesterer.free.fr/regexp/

Source1: visual_regexp.tcl
Source2: README

BuildArch: noarch
Requires: tk

%description
VisualREGEXP helps you to design, debug or more generally work with regular
expression. As it is often difficult to write the right regexp at the first
try, this tool will show you the effect of your regexp on a sample you can
choose.

%prep
%setup -Tc
cp %{SOURCE2} .

%install
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/tkregexp

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc README
