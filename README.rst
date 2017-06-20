====
ezpy
====

 |Travis CI|  |Coveralls|  |GitHub Issues|  |License|
 |Development Status|  |Latest Version|  |Download format|  |Downloads|

Make Python application installs easy as pie, for both users and developers.

.. contents:: **Contents**


.. _setup-start:

Introduction
------------

**TODO**


Usage
-----

**TODO**


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
