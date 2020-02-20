"""
Unit and regression test for the deepdyn package.
"""

# Import package, test suite, and other packages as needed
import deepdyn
import pytest
import sys

def test_deepdyn_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "deepdyn" in sys.modules
