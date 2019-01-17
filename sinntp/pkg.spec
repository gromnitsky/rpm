Summary: A tiny, non-interactive NNTP client
Name: sinntp
Version: 1.6.1
License: GPLv2+
URL: https://github.com/jwilk/sinntp

# git ls-remote https://github.com/jwilk/sinntp HEAD
%global commit0 feeeb7768a14d870dff1a870783c8d999b445d6f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/jwilk/%name/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz

Release: 1.20190117git.%shortcommit0%{?dist}

BuildRequires: python3-devel

%description
* send articles
* fetch new articles into an mbox file
* fetch articles in RFC822 format
* list available newsgroups

%prep
%setup -q -n %name-%commit0

%global dest_dir $RPM_BUILD_ROOT/%_datadir/%name

%build
cd doc/manpages
sed -i.orig 's/nntp-/si\0/g' nntp*xml
make

%install
install -D sinntp -t %dest_dir
mkdir -p $RPM_BUILD_ROOT/%_bindir
ln -sf %_datadir/%name/%name $RPM_BUILD_ROOT%{_bindir}/%name

install -D -m644 plugins.py utils.py -t %dest_dir
install -D -m644 doc/manpages/*.1 -t $RPM_BUILD_ROOT/%_mandir/man1/

# https://fedoraproject.org/wiki/Packaging:Python_Appendix
%py_byte_compile %__python3 %dest_dir

%files
%_bindir/*
%_datadir/*
%_mandir/*
%doc doc/*.txt doc/NEWS
