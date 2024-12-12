Name:    zoo
Version: 2.10
Release: 2%{?dist}
License: GPLv2+
Summary: File archiving utility with compression
Source0: http://www.ibiblio.org/pub/packages/ccic/software/unix/utils/zoo210.tar.gz
# all patches are from Debian
patch01: 01-old-fixes.patch
patch02: 02-traversal-directory.patch
patch03: 03-fix-manage-archive-under-AMD64.patch
patch04: 04-fix-fullpath-buffer-overflow.patch
patch05: 05-CVE-2006-1269.patch
patch06: 06-CVE-2007-1673.patch
patch07: 07-ms-help-reduce-outputted-newlines-in-help.patch
patch08: 08-wait-return-comment-out.patch
patch10: 10-printf.patch
patch12: 12-printf.patch
patch14: 14-printf.patch

%description
zoo is a data compression program and format developed by Rahul Dhesi
in the mid-1980s. The format is based on the LZW compression algorithm
and compressed files are identified by the .zoo file extension. It is
no longer widely used. Program source code was originally published on
the comp.sources.misc.

%prep
%setup -c
%patch -P 01 -p1 -b.orig
%patch -P 02 -p1 -b.orig
%patch -P 03 -p1 -b.orig
%patch -P 04 -p1 -b.orig
%patch -P 05 -p1 -b.orig
%patch -P 06 -p1 -b.orig
%patch -P 07 -p1 -b.orig
%patch -P 08 -p1 -b.orig
%patch -P 10 -p1 -b.orig
%patch -P 12 -p1 -b.orig
%patch -P 14 -p1 -b.orig

%build
unset LDFLAGS
%make_build linux OPTIM='-O -Wno-implicit-int'

%install
install -D fiz -t $RPM_BUILD_ROOT/%_bindir
install -D zoo -t $RPM_BUILD_ROOT/%_bindir
install -D -m644 fiz.1 -t $RPM_BUILD_ROOT/%_mandir/man1/
install -D -m644 zoo.1 -t $RPM_BUILD_ROOT/%_mandir/man1/

%files
%_bindir/*
%{_mandir}/*
