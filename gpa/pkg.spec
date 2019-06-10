%global commit 1cb82dcfcea46878cad353022c8f537d4c9d879d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: GPA is a GUI for the GnuPG
Name: gpa
Version: 0.11.0
License: GPLv3+

URL: https://gnupg.org/software/gpa/index.html
Source0: https://github.com/gpg/gpa/archive/%commit/%name-%shortcommit.tar.gz
Release: 1.20190513git.%shortcommit%{?dist}

BuildRequires: gtk2-devel, gpgme-devel
Requires: gtk2, gpgme

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
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/*/*
%{_datadir}/pixmaps/*
