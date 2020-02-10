A small collection of rpm specs for programs that are missing in the
Fedora repos.

To build an rpm, cd to a specific directory with the .spec file &
type:

	$ make -f ../build.mk download
	$ make -f ../build.mk

If there were no errors, look into `_out/RPMS` directory.

Read comments in `build.mk` file (in the root directory) for other
useful targets.

## TODO

* wkhtmltox
