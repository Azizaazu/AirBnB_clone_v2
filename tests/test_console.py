#!/usr/bin/python3
"""Unittests for console.py"""

from console import HBNBCommand
import unittest
import sys
from io import StringIO
from unittest.mock import patch

class TestConsoleCreateCommand(unittest.TestCase):
    """Test cases for the create command in console.py"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the test environment"""
        del self.console

    def test_create_with_string_parameter(self):
        """Test create command with string parameter"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create User name="John Doe" age=25')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming UUID length is 36

    def test_create_with_float_parameter(self):
        """Test create command with float parameter"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create User weight=150.5')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming UUID length is 36

    def test_create_with_invalid_parameter(self):
        """Test create command with invalid parameter"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create User invalid_param=abc')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** invalid_param doesn't exist **")

if __name__ == "__main__":
    unittest.main()
