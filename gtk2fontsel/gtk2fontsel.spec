Name: gtk2fontsel
Version: 0.1
Release: 1%{?dist}
Summary: A command line version of the GtkFontSelection widget

License: GPLv2
URL: http://gtk2fontsel.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: gtk2-devel

%description
The GTK2 port of an unmainained gtkfontsel.

%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/*
