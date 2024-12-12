Summary: An eye-candy dockapp to monitor Linux ACPI battery status.
Name: wmvolt
Version: 0
License: GPLv2+
URL: https://github.com/gromnitsky/wmvolt

# git ls-remote https://github.com/gromnitsky/wmvolt HEAD
%global commit0 9263517a5ead62fa2eed1438654f3739dce765e2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/gromnitsky/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Release: 1.20241212git.%shortcommit0%{?dist}

BuildRequires: libXext-devel libXpm-devel asciidoc

%description
wmvolt is a program to monitor ACPI battery status (using a "new"
`/sys/class/power_supply/*` interface). It's a dockapp for Window
Managers like Window Maker or FVWM.

%prep
%setup -q -n %{name}-%{commit0}

%build
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
