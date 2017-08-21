Summary: GPA is a GUI for the GnuPG
Name: gpa
Version: 0.9.10
Release: 1%{?dist}
License: GPLv3+
Group: Interface/X

URL: https://gnupg.org/software/gpa/index.html
Source0: ftp://ftp.gnupg.org/gcrypt/gpa//gpa-%{version}.tar.bz2

BuildRequires: gtk2-devel, gpgme-devel
Requires: gtk2, gpgme

%description
GPA is a graphical frontend for the GNU Privacy Guard (GnuPG). GPA can
be used to encrypt, decrypt, and sign files, to verify signatures and
to manage the private and public keys.

%prep
%setup -q

%build
%configure --disable-nls
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_mandir}/*/*
%{_datadir}/pixmaps/*
