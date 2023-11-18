%global commit 12b102444d84f87b6a8556cc39b6d0859bd77179
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: GPA is a GUI for the GnuPG
Name: gpa
Version: 0
License: GPLv3+

URL: https://gnupg.org/software/gpa/index.html
Source0: https://github.com/gpg/gpa/archive/%commit/%name-%shortcommit.tar.gz
Release: 1.20231118git.%shortcommit%{?dist}

BuildRequires: gtk3-devel, gpgme-devel
Requires: gtk3, gpgme

%description
GPA is a graphical frontend for the GNU Privacy Guard (GnuPG). GPA can
be used to encrypt, decrypt, and sign files, to verify signatures and
to manage the private and public keys.

%prep
%autosetup -n %name-%commit
aclocal -I m4
autoheader
automake --foreign
autoconf

%build
%configure --disable-nls
%make_build

%install
%make_install

%files
%_bindir/*
%_datadir/*
