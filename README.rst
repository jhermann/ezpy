====
ezpy
====

 |Travis CI|  |Coveralls|  |GitHub Issues|  |License|
 |Latest Version|

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

.. code-block::

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
* `Share scripts that have dependencies with Nix <https://compiletoi.net/share-scripts-that-have-dependencies-with-nix/>`_

Related Projects
^^^^^^^^^^^^^^^^
Last recorded commit activity is included as ``(YYYY)`` – at the time entries were added (2017).

* `pantsbuild/pex <https://github.com/pantsbuild/pex>`_ (2017) – A library and tool for generating .pex (Python EXecutable) files.
* `getsentry/freight <https://github.com/getsentry/freight>`_ (2017) – A service which aims to make application deployments better.
* `armadaplatform/armada <https://github.com/armadaplatform/armada>`_ (2017) – Complete solution for development, deployment, configuration and discovery of microservices.
* `cloudify-cosmo/wagon <https://github.com/cloudify-cosmo/wagon>`_ (2017) – Creates wheel-based archives to allow portable offline installation of Python packages and their dependencies.
* `mitsuhiko/platter <https://github.com/mitsuhiko/platter>`_ (2015) – A useful helper for wheel deployments.
* `sdispater/poet <https://github.com/sdispater/poet>`_ (2017, experimental) – Declare, manage and install dependencies of Python projects – inspired by ``cargo``.
* `jamesabel/osnap <https://github.com/jamesabel/osnap>`_ (2017) – Deliver self-contained Python applications to end users for Windows and OSX/MacOS.
* `glyph/venvdotapp <https://github.com/glyph/venvdotapp>`_ - Virtualenv to NSBundle (MacOS) packager.
* `mherrmann/fbs <https://github.com/mherrmann/fbs>`_ (2018) – Create cross-platform desktop apps in minutes, not months.

* `flatpak <https://github.com/flatpak/flatpak>`_ (2017) – Linux application sandboxing and distribution framework.
* `jonparrott/noel <https://github.com/jonparrott/noel>`_ (2016) – Easily deploy applications to Kubernetes.
* `0xadada/dockdj <https://github.com/0xadada/dockdj>`_ (2015, unmaintained) – Building 12-factor Python / Django web apps Docker images and deploying them to AWS.
* `mattmakai/underwear <https://github.com/mattmakai/underwear>`_ (2015) – Dead simple LAMP-stack deployments for Python-powered web applications.



.. |Travis CI| image:: https://api.travis-ci.org/jhermann/ezpy.svg
    :target: https://travis-ci.org/jhermann/ezpy
.. |Coveralls| image:: https://img.shields.io/coveralls/jhermann/ezpy.svg
    :target: https://coveralls.io/r/jhermann/ezpy
.. |GitHub Issues| image:: https://img.shields.io/github/issues/jhermann/ezpy.svg
    :target: https://github.com/jhermann/ezpy/issues
.. |License| image:: https://img.shields.io/pypi/l/ezpy.svg
    :target: https://github.com/jhermann/ezpy/blob/master/LICENSE
.. |Development Status| image:: https://img.shields.io/pypi/status/ezpy.svg
    :target: https://pypi.python.org/pypi/ezpy/
.. |Latest Version| image:: https://img.shields.io/pypi/v/ezpy.svg
    :target: https://pypi.python.org/pypi/ezpy/
.. |Download format| image:: https://img.shields.io/pypi/format/ezpy.svg
    :target: https://pypi.python.org/pypi/ezpy/
