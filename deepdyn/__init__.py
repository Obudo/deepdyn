"""
deepdyn
A python package that offers an implementation of deep learning methods for the analysis of dynamical systems.
"""

# Add imports here
from .deepdyn import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
