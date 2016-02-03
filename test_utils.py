# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        with self.assertRaises(ValueError):
            utils.fact(-1)
        self.assertEqual(utils.fact(5),120)
        
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(9,3,4),9)
        pass
    
    def test_integrate(self):
        self.assertEqual(utils.integrate(5,1,2),5)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
