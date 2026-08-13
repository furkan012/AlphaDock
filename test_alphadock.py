# test_alphadock.py
"""
Tests for AlphaDock module.
"""

import unittest
from alphadock import AlphaDock

class TestAlphaDock(unittest.TestCase):
    """Test cases for AlphaDock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlphaDock()
        self.assertIsInstance(instance, AlphaDock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlphaDock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
