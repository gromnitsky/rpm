Name: grap
Version: 1.45
Release: 1%{?dist}
Summary: A language for typesetting graphs

License: BSD
URL: http://www.lunabase.org/~faber/Vault/software/%{name}/
Source0: http://www.lunabase.org/~faber/Vault/software/%{name}/%{name}-%{version}.tar.gz

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
%setup -q

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
