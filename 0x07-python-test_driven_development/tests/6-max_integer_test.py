#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class"""
    def test_module_docstring(self):
        """The tests for module docsting of the function"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """The tests for funstion docstring of the function"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """The tests for empty list [] for the function"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """The tests for no arguments passed to function"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """The tests for only one number in the list of the function"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_end(self):
        """The tests for all positive with max at end of the function"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def test_positive_middle(self):
        """The tests for all positive with max in middle of the function"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def test_positive_beginning(self):
        """The tests for all positive with max at beginning of the function"""
        b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 200)

    def test_one_negative(self):
        """The tests for list with one negative number of the function"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def test_all_negative(self):
        """The tests for list with all negative numbers of the function"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """The tests for passing none as argument of the function"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """The tests for a non-int type in list of the function"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
