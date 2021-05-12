Name: xoris
Version: 0.1e
Release: 2%{?dist}
Summary: Grab a color from the screen & print its value to stdout
License: MIT
URL: http://sourceforge.net/projects/xoris/
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz

Source1: xoris-run.sh

BuildRequires: libX11, imake
Requires: rgb, xmessage

%description
See summary.

%prep
%setup -q


%build
xmkmf
make %{?_smp_mflags}


%install
%make_install
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/*

%doc README
