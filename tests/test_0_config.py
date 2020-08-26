#! /usr/bin/env python3

import os
import unittest
import config

verbose_tests = False


class ConfigTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_data(self):
        self.assertTrue(os.path.exists(config.data_dir))
        self.assertTrue(os.path.isfile(os.path.join(config.data_dir, config.facts_csv)))
        self.assertTrue(os.path.isfile(os.path.join(config.data_dir, config.sources_csv)))
        if verbose_tests: print("TEST:ran test_data")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

