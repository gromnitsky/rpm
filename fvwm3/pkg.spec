# requires: `gem install asciidoctor`, golang

Name: fvwm3
Version: 0
Summary: An ICCCM-compliant multiple virtual desktop window manager
URL: https://github.com/fvwmorg/fvwm3/
License: GPLv2+
Conflicts: fvwm fvwm2

# git ls-remote https://github.com/fvwmorg/fvwm3 HEAD
%global commit0 32c9abcc126428dbd81120ea97820fb8dbf66b21
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/fvwmorg/%name/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz
Release: 1.20210510git.%shortcommit0%{?dist}

Source1: %name.desktop

# copied from the orig fedora spec
Patch2: fvwm-0002-Use-mimeopen-instead-of-EDITOR.patch
Patch3: fvwm-0003-Increase-number-of-mouse-buttons-supported.patch

# https://www.mail-archive.com/fvwm@fvwm.org/msg03147.html
Patch9002: 9002-passthrough-key-action.patch

BuildRequires: autoconf automake
BuildRequires: libbson-devel libevent-devel libX11-devel libXrandr-devel libXrender-devel libXt-devel

# 'opt', but required also
BuildRequires: fontconfig-devel freetype-devel fribidi-devel libpng-devel readline-devel libSM-devel libXcursor-devel libXext-devel libXi-devel libXpm-devel imlib2-devel librsvg2-devel
BuildRequires: sharutils libxslt

Requires: redhat-menus xdg-utils xterm %_bindir/mimeopen
# fvwm-bug
Requires: %_sbindir/sendmail
# fvwm-menu-xlock
Requires: xlockmore

%description
%name is a window manager for X11. It is designed to minimize memory
consumption, provide a 3D look to window frames, and a virtual desktop.

%prep
%setup -q -n %name-%commit0
%patch2 -p1 -b .mimeopen
%patch3 -p1 -b .more-mouse-buttons
%patch9002 -p1 -b .passthrough-key-action

# undo '-Werror=format-security' from /usr/lib/rpm/redhat/macros
%global _warning_options -Wall

%build
./autogen.sh
%configure --enable-mandoc --enable-golang
%make_build

%install
%make_install
install -D -m0644 -p %SOURCE1 %buildroot/%_datadir/xsessions/%name.desktop

%files
%license COPYING
%_bindir/*
%_libexecdir/*
%_datadir/*
