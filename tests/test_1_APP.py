#! /usr/bin/env python3

import unittest
import dogs_fact

verbose_tests = False


class TruckTests(unittest.TestCase):
    def setUp(self):
        self.fact = dogs_fact.get_fact()

    def test_count(self):
        self.assertEqual(len(self.fact), 1)
        if verbose_tests: print("TEST:ran test_count")

    #def test_source(self):
    #    self.assertIsInstance(self.fact[0]['SOURCE'], dict)
    #    if verbose_tests: print("TEST:ran test_source")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

