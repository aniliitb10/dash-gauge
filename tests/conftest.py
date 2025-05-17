import pytest
import os
import sys

# Add the project root directory to the Python path
# This ensures that the tests can import the package correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))