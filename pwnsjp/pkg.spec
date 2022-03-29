Summary: a text-based frontend to some dictionaries published by Wydawnictwo Naukowe PWN
Name: pwnsjp
Version: 0
License: GPLv2+
URL: https://github.com/jwilk/pwnsjp

# git ls-remote https://github.com/jwilk/pwnsjp HEAD
%global commit0 b04db2e255bebd652c262687afd49fd1ac685269
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/jwilk/%name/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz

Release: 1.20220329git.%shortcommit0%{?dist}

BuildRequires: ncurses-devel zlib-devel libxslt automake elinks gperf docbook-style-xsl

patch0: env.patch

%description
The following dictionaries has been tested:

“Słownik języka polskiego”, 3 volumes
 (distributed as an attachment to Gazeta Wyborcza) [3TSJP];
“Multimedialny słownik PWN. Frazeologia” [MSF];
“Multimedialny słownik PWN. Język polski” [MSJP];
“Multimedialny słownik PWN. Wyrazy obce” [MSWO].

You will need the *.win file, which can be obtained:

either by extracting from setup/data1.cab using Unshield;
or by installing the original interface on Windows/Wine.

%prep
%setup -q -n %name-%commit0
%patch0 -p1 -b .env
private/autogen

%global dict_dir $RPM_BUILD_ROOT/%_datadir/%name

%build
%configure
%make_build

%install
%make_install

%files
%_bindir/*
%_datadir/*
