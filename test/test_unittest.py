import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

import unittest
from src import statistics_functions

class TestStatisticsFunctions(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(statistics_functions.fun1([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(statistics_functions.fun1([10, 20, 30]), 20.0)
        self.assertEqual(statistics_functions.fun1([0, 0, 0]), 0.0)
        self.assertEqual(statistics_functions.fun1([-1, 1]), 0.0)

    def test_fun2(self):
        self.assertEqual(statistics_functions.fun2([1, 3, 5]), 3.0)
        self.assertEqual(statistics_functions.fun2([1, 2, 3, 4]), 2.5)
        self.assertEqual(statistics_functions.fun2([7]), 7.0)
        self.assertEqual(statistics_functions.fun2([-3, -1, 1, 3]), 0.0)

    def test_fun3(self):
        self.assertAlmostEqual(statistics_functions.fun3([2, 4, 4, 4, 5, 5, 7, 9]), 2.14, places=2)
        with self.assertRaises(ValueError):
            statistics_functions.fun3([5])

    def test_fun4(self):
        result = statistics_functions.fun4([1, 2, 3, 4, 5])
        self.assertEqual(result["mean"], 3.0)
        self.assertEqual(result["median"], 3.0)
        self.assertIn("std_dev", result)

        result2 = statistics_functions.fun4([10, 20, 30])
        self.assertEqual(result2["mean"], 20.0)
        self.assertEqual(result2["median"], 20.0)

if __name__ == '__main__':
    unittest.main()