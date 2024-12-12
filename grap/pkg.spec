Name: grap
Version: 0
Summary: A language for typesetting graphs
License: BSD
URL: http://www.lunabase.org/~faber/Vault/software/%{name}/

# git ls-remote https://github.com/snorerot13/grap HEAD
%global commit0 4cddf5801e9f83840a2c6cad425aefcdb9009aac
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/snorerot13/grap/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz
Release: 1.20241212git.%shortcommit0%{?dist}

BuildRequires: bison, flex

%description
Grap is a language for typesetting graphs specified and first
implemented by Brian Kernighan and Jon Bentley at Bell Labs. It is an
expressive language for describing graphs and incorporating them in
typeset documents. It is implemented as a preprocessor to Kernigan's pic
language for describing languages, so any system that can use pic can
use grap. For sure, TeX and groff can use it.

Original tutorial: http://www.kohala.com/start/troff/cstr114.ps

%prep
%setup -q -n %name-%commit0
aclocal
autoheader
automake --add-missing
autoconf

%build
%configure --with-example-dir=%{_docdir}/%{name}/examples
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_docdir}/*
%{_mandir}/*
%{_datarootdir}/%{name}/*
