Summary: A manpage compiler toolset
Name: mandoc
Version: 0
Epoch: 100
License: ISC
URL: https://mandoc.bsd.lv/

# cvs -d anoncvs@mandoc.bsd.lv:/cvs co mandoc
# tar cfz mandoc-`date +%F-%s`.tar.gz mandoc && rm -rf mandoc
Source0: %name-2020-08-08-1596901228.tar.gz

Release: 1.20200808cvs.1596901228%{?dist}

BuildRequires: zlib-devel

%description
mandoc is a suite of tools compiling mdoc, the roff macro language of
choice for BSD manual pages, and man, the predominant historical
language for UNIX manuals. The main component of the toolset is the
mandoc utility program that formats output for UTF-8 and ASCII UNIX
terminals, HTML 5, PostScript, and PDF.

%prep
%setup -q -n %{name}

%build
./configure
make

%install
install -D mandoc demandoc -t $RPM_BUILD_ROOT/%_bindir/
install -D -m644 mandoc.1 demandoc.1 -t $RPM_BUILD_ROOT/%_mandir/man1/

%files
%_bindir/*
%_mandir/*
