#!/usr/bin/env python
# Copyright (C) 2019-2021 Estonian Information System Authority.
# See the file 'LICENSE' for copying permission.

import setuptools
import sys

if sys.version[0] == "2":
    sys.exit(
        "The latest version of Cuckoo is Python >=3.6 only. Any Cuckoo version "
        "earlier than 3.0.0 supports Python 2."
    )

setuptools.setup(
    name="Cuckoo-machineries",
    author="",
    author_email="",
    packages=setuptools.find_namespace_packages(include=["cuckoo.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
    url="https://cuckoosandbox.org/",
    license="GPLv3",
    description="Cuckoo machinery modules and helpers",
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "Cuckoo-common>=0.1.1",
    ],
)
