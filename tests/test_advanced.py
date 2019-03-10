# -*- coding: utf-8 -*-

from .context import examples

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(examples.hmm())

    def test_gethmm(self):
        self.assertEqual(examples.get_hmm(),"hmmm...")


if __name__ == '__main__':
    unittest.main()
