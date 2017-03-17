# Requires: rpmdevtools, rpm-build, rpmlint
#
# A sequence of targets 'patch' <- 'compile' <- 'install' <- 'rpm' is
# equal to 'build' target.
#
# Use OPTS variable for additional build options, e.g.:
#
# % make target OPTS='--with=foo'
#
# 'spec-dump' target supports OPTS variable also:
#
# % make spec-dump OPTS='-D "_without_x --without-x"' | less
#
# To create debug rpms, pass 'DEBUG=1'.

# command line flags
OPTS :=
DEBUG :=

ROOT := $(CURDIR)/rpmbuild
LOGS := $(CURDIR)/logs
SRC := $(CURDIR)
SPEC := $(word 1,$(wildcard *.spec))

# options for rpmbuild
macros := -D "_topdir $(ROOT)" -D "_sourcedir $(SRC)" -D "_specdir $(SRC)"
dpkg :=
ifndef DEBUG
dpkg := -D "debug_package %{nil}"
endif

all: build

.PHONY: tree clean-tree clean build patch compile install rpm \
	spec-check spec-dump download clean-rpm

tree: clean-tree
	mkdir -p $(ROOT)/{BUILD,BUILDROOT,RPMS,SRPMS} $(LOGS)

clean-tree:
	rm -rf $(ROOT) $(LOGS)

clean: tree

build: clean
	rpmbuild $(macros) $(dpkg) -ba $(SPEC) $(OPTS) \
		2>&1 | tee $(LOGS)/all

patch: clean
	rpmbuild $(macros) -bp $(SPEC) $(OPTS) \
		2>&1 | tee $(LOGS)/0-patch

compile:
	rpmbuild $(macros) -bc --short-circuit $(SPEC) $(OPTS) \
		2>&1 | tee $(LOGS)/1-compile

install:
	rpmbuild $(macros) $(dpkg) -bi --short-circuit $(SPEC) $(OPTS) \
		2>&1 | tee $(LOGS)/2-install

rpm: install
	rpmbuild $(macros) $(dpkg) -bb --short-circuit $(SPEC) $(OPTS) \
		2>&1 | tee $(LOGS)/3-rpm

srpm: install
	rpmbuild $(macros) $(dpkg) -bs --short-circuit $(SPEC) $(OPTS) \
		2>&1 | tee $(LOGS)/3-srpm

spec-check:
	rpmbuild $(macros) --nobuild --nodeps $(SPEC)

spec-lint:
	rpmlint -v $(SPEC)

spec-dump:
	rpmspec $(macros) $(OPTS) -P $(SPEC)

download:
	spectool -g $(SPEC)

clean-rpm:
	rm -rf $(ROOT)/*RPMS/*
