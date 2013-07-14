Name: xoris
Version: 0.1e
Release: 1%{?dist}
Summary: Grabs color from the screen & dumps it to stdout
Group: Applications/Productivity
License: MIT
URL: http://sourceforge.net/projects/xoris/
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz

Source1: xoris-run.sh

BuildRequires: libX11, imake
Requires: xorg-x11-server-utils, xorg-x11-apps

%description
See summary.

%prep
%setup -q


%build
xmkmf
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/*

%doc README


%changelog
