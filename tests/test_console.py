#!/usr/bin/python3
"""
Test class
"""

import unittest
from unittest.mock import patch
from io import StringIO
import console
import unittest
HBNBCommand = console.HBNBCommand


class TestDoCreateMethod(unittest.TestCase):

    def setUp(self):
        self.obj = console()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        self.obj.do_create("create State name=\"California\"")
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_create_instance_with_attributes(self):
        expected_output = "New instance created: <instance_id>"
        self.assert_stdout(expected_output)

        # Add additional assertions if needed, e.g., check if the instance is
        # actually created

    def test_create_instance_missing_class_name(self):
        expected_output = "** class name missing **"
        self.assert_stdout(expected_output)

    def test_create_instance_invalid_class_name(self):
        expected_output = "** class 'InvalidClass' doesn't exist **"
        self.assert_stdout(expected_output)

    def test_create_instance_invalid_number_of_arguments(self):
        expected_output = "** invalid number of arguments **"
        self.assert_stdout(expected_output)

    def test_create_instance_invalid_attribute_value(self):
        expected_output = "New instance created: <instance_id>"
        with patch('builtins.input', side_effect=['create State invalid_attribute="123"']):
            self.assert_stdout(expected_output)

        # Add additional assertions if needed, e.g., check if the instance is
        # actually created


if __name__ == '__main__':
    unittest.main()
