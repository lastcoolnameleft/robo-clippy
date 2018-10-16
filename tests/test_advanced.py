# -*- coding: utf-8 -*-

from .context import robo_clippy

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(robo_clippy.hmm())


if __name__ == '__main__':
    unittest.main()
