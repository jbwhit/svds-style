# -*- coding: utf-8 -*-

import unittest

import mplsvds


class Tests(unittest.TestCase):

    def test_oranges(self):
        self.assertEqual(len(mplsvds.oranges), 4)

    def test_hex2rgb(self):
        self.assertListEqual(
            mplsvds.hex2rgb(['#123ABC', '#000000', '#FFFFFF']),
            [(18, 58, 188), (0, 0, 0), (255, 255, 255)])

    def test_norm_rgb(self):
        self.assertEqual(
            mplsvds.norm_rgb([(0, 51, 255)]),
            [(0.0, 0.2, 1.0)])

if __name__ == '__main__':
    unittest.main()
