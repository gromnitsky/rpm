Summary: An eye-candy dockapp to monitor Linux ACPI battery status.
Name: wmvolt
Version: 0.0.1%{?dist}
Release: 1
License: GPLv2+
URL: https://github.com/gromnitsky/wmvolt

# https://fedoraproject.org/wiki/Packaging:SourceURL
%global commit0 a5b245a7f647d7c536e92bcac4f83e5bd0ae0262
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
