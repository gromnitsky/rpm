Summary: Find and remove unnecessary includes in C or C++ source files
Name: deheader
Version: 0
License: BSD-2-Clause
URL: https://gitlab.com/esr/deheader

# git ls-remote https://gitlab.com/esr/deheader.git HEAD
%global commit 3f16cc71168eb52d46ae0d7ad8fe0063b12b6e8d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source0: https://gitlab.com/esr/%name/-/archive/%commit/%name-%commit.tar.gz
Release: 1.20260810git.%shortcommit%{?dist}

%description
deheader analyzes C and C files to determine which header inclusions can be
removed while still allowing them to compile.  This may result in substantial
improvements in compilation time, especially on large C projects; it also
sometimes exposes dependencies and cohesions of which developers were unaware.

%prep
%setup -q -n %name-%commit

%build
%make_build

%install
%make_install PREFIX=/usr

%files
%_bindir/*
%_mandir/*/*
