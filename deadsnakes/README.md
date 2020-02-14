# Deadsnakes PPA Builds for Debian in Docker

## What's a dead snake?

The [Deadsnakes PPA](https://github.com/deadsnakes) project
originally built older Python releases for Ubuntu,
so you could e.g. run unit tests on a new release
using a Python version found on older releases (i.e. the ‘dead’ snakes).

Nowadays, the project also builds *newer* Python versions
ahead of what a certain release offers as its default,
but sticks to its established name.

The packages contain the minor Python version in their name (e.g. `python3.6`)
and can thus be installed concurrently to the default `python3` ones,
and also other minor versions.
Originally based on the Debian source packages,
they can still be built on Debian and not just on Ubuntu.


## What is this then?

This directory contains a Dockerfile that builds
packages for some Debian releases based on the
[Deadsnakes PPA](https://github.com/deadsnakes) code,
by running the build process in the related base image.

If you want pre-built packages that could be APT-installed directly from Bintray,
[show your interest](https://github.com/jhermann/ezpy/issues/3) by voting on issue #3.


## What did you try so far?

These combinations were tested and end up in successful builds:

* ``./build.sh debian:stretch python3.6``
* ``./build.sh debian:buster  python3.6``
* ``./build.sh debian:stretch python3.7``
* Buster comes with 3.7.3 on board
* ``./build.sh debian:stretch python3.8``
* ``./build.sh debian:buster  python3.8``

Based on this and as of February 2020,
*Python 3.6* can be used on Stretch, Buster, and Xenial,
as a set of the usual core Python packages
(`python3.6`, `python3.6-venv`, `python3.6-dev`, …).
Note that Bionic comes with 3.6 as a default.

The same goes for *Python 3.7*, with Buster having it as a default.

*Python 3.8* is an add-on for all the (old-)stable releases.

As a negative example, Python 3.6 on Jessie does not work
because of a ``Breaks: libmpdec2 (<< 2.4.2)`` control file entry
for the stdlib package (and Jessie comes with 2.4.1).
