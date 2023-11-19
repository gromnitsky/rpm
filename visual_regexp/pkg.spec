Summary: Graphical front-end to write/debug regular expressions
Name: visual-regexp
Version: 3.1
Release: 1%{?dist}
License: GPLv2+
URL: http://laurent.riesterer.free.fr/regexp/

Source0: http://laurent.riesterer.free.fr/regexp/visual_regexp-3.1.tcl
Source1: tkregexp.desktop

patch1: font.patch

BuildArch: noarch
Requires: tk, tcl-tclvfs
BuildRequires: dos2unix

%description
VisualREGEXP helps you to design, debug or more generally work with regular
expression. As it is often difficult to write the right regexp at the first
try, this tool will show you the effect of your regexp on a sample you can
choose.

%prep
%setup -Tc
cp %{SOURCE0} .
%patch -P 1 -p0 -b .font
dos2unix visual_regexp-3.1.tcl

%install
install -D visual_regexp-3.1.tcl -m0755 %buildroot/%_bindir/tkregexp
install -D -m0644 %{SOURCE1} -t %buildroot/%_datadir/applications/

%files
%_bindir/*
%_datadir/*
