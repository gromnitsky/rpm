Summary: A manpage compiler toolset
Name: mandoc
Version: 0
Epoch: 100
License: ISC
URL: https://mandoc.bsd.lv/

# CVS_RSH=ssh cvs -d :ext:anoncvs@mandoc.bsd.lv:/cvs co mandoc
# tar cfz mandoc-`date +%F-%s`.tar.gz mandoc && rm -rf mandoc
Source0: %name-2023-11-18-1700293364.tar.gz

Release: 2.20231118cvs.1700293364%{?dist}

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
echo PREFIX=/usr > configure.local
./configure
%make_build

%install
#make install DESTDIR=$RPM_BUILD_ROOT
install -D mandoc demandoc -t $RPM_BUILD_ROOT/%_bindir/
install -D -m644 mandoc.1 demandoc.1 -t $RPM_BUILD_ROOT/%_mandir/man1/
install -D -m644 mandoc.css -t $RPM_BUILD_ROOT/%_datadir/misc/

%files
%_bindir/*
%_datadir/*
