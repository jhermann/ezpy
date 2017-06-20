#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, invalid-name, wrong-import-position
"""
    ezpy - Make Python application installs easy as pie, for both users and developers.

    This setuptools script follows the DRY principle and tries to
    minimize repetition of project metadata by loading it from other
    places (like the script module's ``__*__`` attributes). Incidently,
    this makes the script almost identical between different projects.

    It is also importable (by using the usual ``if __name__ == '__main__'``
    idiom), and exposes the project's setup data in a ``project`` dict.
    This allows other tools to exploit the data assembling code contained
    in here, and again supports the DRY principle. The ``rituals`` package
    uses that to provide Invoke tasks that work for any project, based on
    its project metadata.

    Copyright ©  2017 Jürgen Hermann <jh@web.de>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

project = dict(
    name='ezpy',
    url='https://github.com/jhermann/ezpy',
    license="Apache 2.0",
    keywords='install deploy pip packaging virtualenv hosted.by.github',
    py_modules=['ezpy'],

    install_requires=[],

    entry_points={
        "console_scripts": [
            "ezpy = ezpy:run",
        ],
    },

    # Added by the code below:
    #   version author author_email (from script module)
    #   description (from doc string above)
    #   long_description (from README)
    #   classifiers (see below)
)

classifiers = """
# Details at http://pypi.python.org/pypi?:action=list_classifiers
Development Status :: 3 - Alpha
#Development Status :: 4 - Beta
#Development Status :: 5 - Production/Stable
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.4
Environment :: Console
Intended Audience :: End Users/Desktop
Intended Audience :: Developers
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Topic :: Software Development
Topic :: System :: Installation/Setup
Topic :: System :: Software Distribution
Topic :: Utilities
"""

# Beyond this point, code is not project-specific
import io
import os
import re
import sys
import json

try:
    from setuptools import setup
except ImportError as exc:
    raise RuntimeError("Cannot install '{0}', setuptools is missing ({1})"
                       .format(project['name'], exc))

project_root = os.path.abspath(os.path.dirname(__file__))
script_name = os.path.join(project_root, project['py_modules'][0] + '.py')
expected_keys = "version author author_email".split()
with io.open(script_name, encoding='utf-8') as handle:
    for line in handle:
        match = re.match(r"""^__({})__ += (?P<q>['"])(.+?)(?P=q)$"""
                         .format('|'.join(expected_keys)), line)
        if match:
            project[match.group(1)] = match.group(3)

project.update(dict(
    description=__doc__.split('.')[0].split(' - ', 1)[1].strip(),
    long_description=(io.open('README.rst', encoding='UTF-8').read()
                      .split('\n.. _setup-start:', 1)[-1].strip()),
    classifiers=[i.strip()
                 for i in classifiers.splitlines()
                 if i.strip() and not i.strip().startswith('#')],
    keywords=project['keywords'].replace(',', ' ').strip().split(),
))

# Ensure 'setup.py' is importable by other tools, to access the project's metadata
__all__ = ['project', 'project_root']
if __name__ == '__main__':
    if '--metadata' in sys.argv[:2]:
        json.dump(project, sys.stdout, default=repr, indent=4, sort_keys=True)
        sys.stdout.write('\n')
    else:
        setup(**project)
