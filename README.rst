====
ezpy
====

 |Travis CI|  |Coveralls|  |GitHub Issues|  |License|
 |Latest Version|  |Downloads|

Make Python application installs easy as pie, for both users and developers.

.. contents:: **Contents**


.. _setup-start:

Introduction
------------

What Does it Do?
^^^^^^^^^^^^^^^^

The main goal of the project is to make installs very easy and convenient,
without abandoning security and other technical requirements.
Think ``pipsi`` with a wider scope, and working on Python 3.


Design Goals
^^^^^^^^^^^^

* Reduce installation instructions to ideally one or two command calls
* Make distribution of ‘simple’ scripts a breeze

  * … but support dependencies from PyPI nontheless

* Require only a Python interpreter to be already installed on an end-user machine

  * … but use what's installed already (if new enough)
  * Work on outdated installations (say down to Wheezy / Precise / pip 1.5.6)

* Work on Linux, MacOS, Windows (in that order of importance)
* Rely heavily on existing tooling, especially ``pyvenv`` and ``pip``
* Vendor any dependencies, or don't have any beyond the standard library.


Usage
-----

End-Users
^^^^^^^^^

Story ♯1: Users can download a simple script and start it (or, well, ``curl|python`` it),
and it'll bootstrap a full environment of dependencies.

Story ♯2: Users need to ``pip3 install --user ezpy``.
Calling ``python3 -m ezpy check`` after that will go around any OS shenanigans
– that could be used to handle the ``~/.local/bin`` problem (``python3 -m ezpy fix-path``).

Given no dependencies, ``sudo pip3 install ezpy`` would also be ok.
And this is another option for bootstrapping:

.. code:

    pip install -t /tmp/$USER-$$ ezpy
    python /tmp/$USER-$$/ezpy.py bootstrap

Then users are able to install any
PyPI application or tool via a simple call to ``ezpy get|run ‹requirement|script-url›``.
Mostly like ``pipsi`` operates.
Console entry points are linked / copied into the existing path, leaving out any unrelated
virtualenv binaries (including Python itself).

Story ♯3: ``ezpy run ‹url›#‹algo›=‹checksum›`` to directly run scripts from the web
– security is based on the trust you have into the 3rd party
that gave you the link with the checksum.
No difference to PyPI installs secured by a checksum – those run downloaded code, too.

Story ♯4: ``ezpy docker run …``


Developers
^^^^^^^^^^

Relating to ♯1, give developers the ability to embed code
that intercepts command calls (``myscript ezpy …``).
They call ``ezpy embed ‹myscript.py›``, and a stub is added that does this.

For #2, nothing special has to be done. Just release normally to PyPI,
or make a script available via a HTTP[S] URL.

♯4: Something like ``ezpy docker build …`` or ``ezpy docker-file …``.


Installation
------------

*ezpy* can be installed via ``pip install ezpy`` as usual,
see `releases <https://github.com/jhermann/ezpy/releases>`_ for an overview of available versions.
To get a bleeding-edge version from source, use these commands::

    repo="jhermann/ezpy"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"

As a developer, to create a working directory for this project, call these commands::

    git clone "https://github.com/jhermann/ezpy.git"
    cd "ezpy"
    command . .env --yes --develop  # add '--virtualenv /usr/bin/virtualenv' for Python2
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.


References
----------

* `pip issue #3813 <https://github.com/pypa/pip/issues/3813>`_



.. |Travis CI| image:: https://api.travis-ci.org/jhermann/ezpy.svg
    :target: https://travis-ci.org/jhermann/ezpy
.. |Coveralls| image:: https://img.shields.io/coveralls/jhermann/ezpy.svg
    :target: https://coveralls.io/r/jhermann/ezpy
.. |GitHub Issues| image:: https://img.shields.io/github/issues/jhermann/ezpy.svg
    :target: https://github.com/jhermann/ezpy/issues
.. |License| image:: https://img.shields.io/pypi/l/ezpy.svg
    :target: https://github.com/jhermann/ezpy/blob/master/LICENSE
.. |Development Status| image:: https://pypip.in/status/ezpy/badge.svg
    :target: https://pypi.python.org/pypi/ezpy/
.. |Latest Version| image:: https://img.shields.io/pypi/v/ezpy.svg
    :target: https://pypi.python.org/pypi/ezpy/
.. |Download format| image:: https://pypip.in/format/ezpy/badge.svg
    :target: https://pypi.python.org/pypi/ezpy/
.. |Downloads| image:: https://img.shields.io/pypi/dw/ezpy.svg
    :target: https://pypi.python.org/pypi/ezpy/
