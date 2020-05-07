Summary: A maintained ctags implementation
Name: universal-ctags
Version: 0
License: GPLv2+
URL: https://github.com/universal-ctags/ctags

# https://fedoraproject.org/wiki/Packaging:SourceURL
%global commit0 3671ad7255885a0c8f6ff4979d80c70f201ea411
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/universal-ctags/ctags/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Release: 1.20200502git.%shortcommit0%{?dist}

BuildRequires: autoconf, python3-docutils
BuildRequires: jansson, libxml2, libyaml, libseccomp
Conflicts: ctags
Provides: ctags

%description
Universal Ctags improves on traditional ctags because of its
multilanguage support, its ability for the user to define new
languages searched by regular expressions, and its ability to generate
emacs-style TAGS files.

%prep
%setup -q -n ctags-%{commit0}

%build
./autogen.sh
%configure --enable-etags --disable-readcmd
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*
