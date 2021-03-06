import os
import sys
from fnmatch import fnmatchcase
from distutils.util import convert_path
from setuptools import setup, find_packages


# Provided as an attribute, so you can append to these instead
# of replicating them:
standard_exclude = ("*.py", "*.pyc", "*$py.class", "*~", ".*", "*.bak")
standard_exclude_directories = (".*", "CVS", "_darcs", "./build",
                                "./dist", "EGG-INFO", "*.egg-info")

# (c) 2005 Ian Bicking and contributors; written for Paste (http://pythonpaste.org)
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
# Note: you may want to copy this into your setup.py file verbatim, as
# you can't import this from another package, when you don't know if
# that package is installed yet.


def find_package_data(
    where=".", package="",
    exclude=standard_exclude,
    exclude_directories=standard_exclude_directories,
    only_in_packages=True,
    show_ignored=False):
    """\
Return a dictionary suitable for use in ``package_data``
in a distutils ``setup.py`` file.

The dictionary looks like::

{"package": [files]}

Where ``files`` is a list of all the files in that package that
don"t match anything in ``exclude``.

If ``only_in_packages`` is true, then top-level directories that
are not packages won't be included (but directories under packages
will).

Directories matching any pattern in ``exclude_directories`` will
be ignored; by default directories with leading ``.``, ``CVS``,
and ``_darcs`` will be ignored.

If ``show_ignored`` is true, then all the files that aren't
included in package data are shown on stderr (for debugging
purposes).

Note patterns use wildcards, or can be exact paths (including
leading ``./``), and all searching is case-insensitive.
"""

    out = {}
    stack = [(convert_path(where), "", package, only_in_packages)]
    while stack:
        where, prefix, package, only_in_packages = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "Directory %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                if (os.path.isfile(os.path.join(fn, "__init__.py"))
                    and not prefix):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + "." + name
                    stack.append((fn, "", new_package, False))
                else:
                    stack.append((fn, prefix + name + "/", package, only_in_packages))
            elif package or not only_in_packages:
                # is a file
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "File %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix + name)
    return out


VERSION = __import__("podcasting").__version__

setup(
    name="django-podcasting",
    version=VERSION,
    url="http://django-podcasting.readthedocs.org/",
    license="BSD",
    description="Audio podcasting functionality for django sites.",
    long_description=open("README.rst").read(),
    author="Thomas Schreiber",
    author_email="tom@insatsu.us",
    packages=find_packages(),
    package_data=find_package_data("podcasting", only_in_packages=False),
    install_requires=[
        "django-licenses==0.2.3",
    ],
    tests_require=[
        "django-nose==1.0",
        "Django>=1.3",
        "milkman==0.4.5",
        "PIL==1.1.7",
    ],
    test_suite="podcasting.tests.runtests.runtests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
