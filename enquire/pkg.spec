Summary: Print many properties of the C compiler and the machine
Name: enquire
Version: 5.1a
Release: 1%{?dist}
License: Weird

URL: http://homepages.cwi.nl/~steven/enquire.html
Source0: http://homepages.cwi.nl/~steven/enquire/enquire.c
Source1: http://homepages.cwi.nl/~steven/enquire/enquire.html

%description
Everything you wanted to know about your C Compiler and Machine, but
didn't know who to ask, such as minimum and maximum [un]signed
char/int/long, many properties of float/ [long] double, and so on.

One day Richard Stallman passed by, and mentioned that they needed
such a program for GCC.

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
cc enquire.c -O0 -o enquire

%install
install -D enquire -t $RPM_BUILD_ROOT/%{_bindir}

%files
%defattr(-,root,root,-)
%doc enquire.*
%{_bindir}/*
