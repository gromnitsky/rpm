The RPM of open-vm-tools is a subset of the VMware Tools, currently
composed of user-space programs for Fedora 17+ guest operating systems.

This RPM does not contain kernel & fuse modules.  Unity support is
disabled by upstream.

To build version that doesn't require X11, type:

    $ make build OPTS='--without=x'
