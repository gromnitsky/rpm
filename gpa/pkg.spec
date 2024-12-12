Summary: GPA is a GUI for the GnuPG
Name: gpa
Version: 0
License: GPLv3+
URL: https://gnupg.org/software/gpa/index.html

# git ls-remote https://github.com/gpg/gpa HEAD
%global commit 7421dfa153c263ef9c797a008456308ac5529146
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source0: https://github.com/gpg/gpa/archive/%commit/%name-%shortcommit.tar.gz
Release: 1.20241212git.%shortcommit%{?dist}

patch1: cm-piv.patch

BuildRequires: gtk3-devel, gpgme-devel
Requires: gtk3, gpgme

%description
GPA is a graphical frontend for the GNU Privacy Guard (GnuPG). GPA can
be used to encrypt, decrypt, and sign files, to verify signatures and
to manage the private and public keys.

%prep
%setup -q -n %name-%commit
%patch -P 1 -p0 -b .orig
./autogen.sh

%build
%configure --disable-nls
%make_build

%install
%make_install

%files
%_bindir/*
%_datadir/*
