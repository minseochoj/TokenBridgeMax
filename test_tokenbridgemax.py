# test_tokenbridgemax.py
"""
Tests for TokenBridgeMax module.
"""

import unittest
from tokenbridgemax import TokenBridgeMax

class TestTokenBridgeMax(unittest.TestCase):
    """Test cases for TokenBridgeMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenBridgeMax()
        self.assertIsInstance(instance, TokenBridgeMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenBridgeMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
