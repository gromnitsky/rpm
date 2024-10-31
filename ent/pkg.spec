Summary: A Pseudorandom Number Sequence Test
Name: ent
Version: 0
License: Public domain
URL: https://github.com/Fourmilab/ent_random_sequence_tester

# git ls-remote https://github.com/Fourmilab/ent_random_sequence_tester HEAD
%global commit0 388d2cc499813e6865e833a66b612172a1674efc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Source0: https://github.com/Fourmilab/ent_random_sequence_tester/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz

patch01: randtest.patch
patch02: totalcount.patch

Release: 1.20241031git.%shortcommit0%{?dist}

BuildRequires: w3m

%description
ent performs a variety of tests on the stream of bytes: entropy,
chi-square test, arithmetic mean, Monte Carlo value for Pi, serial
correlation coefficient.

%prep
%setup -q -n ent_random_sequence_tester-%commit0
cd src
%patch 1 -b.orig
%patch 2 -b.orig

%build
cd src
make
w3m -dump -T text/html -O ascii < ent.html > ent.txt

%install
cd src
install -p ent -D -t $RPM_BUILD_ROOT%{_bindir}
install -m 644 -p ent.txt -D -t $RPM_BUILD_ROOT%{_datadir}/doc/%name/

%files
%_bindir/*
%_datadir/*
