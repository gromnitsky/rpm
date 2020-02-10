# Requires (Fedora): rpmdevtools, rpm-build, rpmlint
#
# A sequence of targets 'prep ← build ← install ← rpm' is an rough
# equivalent to 'all' target.
#
# Use 'o' variable for additional options, e.g.:
#
# $ make o=--with=foo
# $ make o=--without=bar
#
# 'spec' target supports 'o' variable also:
#
# $ make spec o='-D "_without_x --without-x"'
#
# For debug rpms, pass 'debug=1'. To preserve BUILDROOT, pass o=--no-clean

# user opts
o :=
debug :=



topdir := $(CURDIR)/_out
log := $(topdir)/log
src := $(CURDIR)
specfile := $(firstword $(wildcard *.spec))

# options for rpmbuild
macros := -D '_topdir $(topdir)' -D '_sourcedir $(src)' -D '_specdir $(src)'
ifndef debug
macros += -D 'debug_package %nil'
endif

all: clean                      # rpm & srpm
	rpmbuild $(macros) -ba $(specfile) $(o) 2>&1 | tee $(log)/all

.PHONY: clean clean-rpm
clean:
	rm -rf $(topdir)
	@mkdir -p $(log)
clean-rpm:; rm -rf $(topdir)/*RPMS/*

prep: clean
	rpmbuild $(macros) -bp $(specfile) $(o) 2>&1 | tee $(log)/0.prep

.PHONY: build
build:
	rpmbuild $(macros) -bc --short-circuit $(specfile) $(o) 2>&1 | \
		tee $(log)/1.build

.PHONY: install
install:
	rpmbuild $(macros) -bi --short-circuit $(specfile) $(o) 2>&1 | \
		tee $(log)/2.install

.PHONY: rpm
rpm:
	rpmbuild $(macros) -bb --short-circuit $(specfile) $(o) 2>&1 | \
		tee $(log)/3.rpm

.PHONY: srpm
srpm:
	rpmbuild $(macros) -bs --short-circuit $(specfile) $(o) 2>&1 | \
		tee $(log)/3.srpm

.PHONY: check lint spec download
check:; rpmbuild $(macros) --nobuild $(o) $(specfile)
lint:; rpmlint -v $(specfile)
spec:; @rpmspec $(macros) $(o) -P $(specfile) | cat -s | sed '/^%changelog/,$$d' | less
download:; spectool -g $(specfile)
