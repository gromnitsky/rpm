Summary: An eye-candy dockapp to monitor Linux ACPI battery status.
Name: wmvolt
Version: 0.0.2
Release: 1%{?dist}
License: GPLv2+
URL: https://github.com/gromnitsky/wmvolt

# https://fedoraproject.org/wiki/Packaging:SourceURL
%global commit0 a8796635c658e46cfc2d4346a8432ae0de6b6977
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/gromnitsky/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

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
