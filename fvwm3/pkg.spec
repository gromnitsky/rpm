# requires: `gem install asciidoctor`, golang

Name: fvwm3
Version: 0
Epoch: 1
Release: 1

Summary: An ICCCM-compliant multiple virtual desktop window manager
URL: https://github.com/fvwmorg/fvwm3/
License: GPLv2+
Conflicts: fvwm fvwm2

%global forgeurl0 https://github.com/fvwmorg/fvwm3
# git ls-remote https://github.com/fvwmorg/fvwm3 HEAD
%global commit0 3abfb28bacf38d34feb3038a7ed6349e575ba5fa

%forgemeta -a
Source0: %{forgesource0}

Source1: %name.desktop

patch1: 682.patch
# copied from the orig fedora spec
Patch2: fvwm-0002-Use-mimeopen-instead-of-EDITOR.patch

BuildRequires: meson
BuildRequires: cjson-devel libevent-devel libX11-devel libXrandr-devel libXrender-devel libXt-devel xorg-x11-xtrans-devel

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
%forgesetup -a

# undo '-Werror=format-security' from /usr/lib/rpm/redhat/macros
%global _warning_options -Wall

%build
%meson -Dmandoc=true -Dnls=disabled -Dgolang=enabled
%meson_build

%check

%install
%meson_install
install -D -m0644 -p %SOURCE1 %buildroot/%_datadir/xsessions/%name.desktop

%files
%license COPYING
%_bindir/*
%_libexecdir/*
%_datadir/*
