Summary: A tool for reverse engineering Android apk files
Name: apktool
Version: 2.10.0
Release: 1%{?dist}
License: ASL 2.0

URL: https://ibotpeaches.github.io/Apktool/
Source0: https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_%{version}.jar

BuildArch: noarch
Requires: java-headless
BuildRequires: javapackages-tools

%description
A tool for reverse engineering 3rd party, closed, binary Android
apps. It can decode resources to nearly original form and rebuild them
after making some modifications. It also makes working with an app
easier because of the project like file structure and automation of
some repetitive tasks like building apk, etc.

%install
install -D -m 644 %{SOURCE0} $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
%jpackage_script brut.apktool.Main "" "" %{name} %{name} true

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_javadir}/*
