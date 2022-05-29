__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

__version__ = "0.0.11"
AUTHOR = "Vanessa Sochat"
EMAIL = "vsoch@users.noreply.github.com"
NAME = "ohno"
PACKAGE_URL = "https://github.com/vsoch/ohno"
KEYWORDS = "error, capture, submission"
DESCRIPTION = "A command line client, wrapper, and Python module for formatting errors."
LICENSE = "LICENSE"

################################################################################
# Global requirements

INSTALL_REQUIRES = ()

TESTS_REQUIRES = (
    ("pytest", {"min_version": "4.6.2"}),
    ("jinja2", {"min_version": None}),
    ("archspec", {"min_version": None}),
)

################################################################################
# Submodule Requirements

INSTALL_REQUIRES_ALL = INSTALL_REQUIRES + TESTS_REQUIRES
