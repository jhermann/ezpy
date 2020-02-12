# Deadsnakes PPA Builds for Debian in Docker

This directory contains a Dockerfile that builds
packages for some Debian releases based on the
[Deadsnakes PPA](https://github.com/deadsnakes) code.

These combinations were tested and end up in successful builds:

* ``./build.sh debian:stretch python3.6``
* ``./build.sh debian:buster  python3.6``
* ``./build.sh debian:stretch python3.7``
* ``./build.sh debian:buster  python3.8``

As a negative example, Python 3.6 on Jessie does not work
because of a ``Breaks: libmpdec2 (<< 2.4.2)`` control file entry
for the stdlib package (and Jessie comes with 2.4.1).
