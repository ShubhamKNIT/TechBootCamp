import unittest

sq = lambda x : x ** 2

class LambdaTest(unittest.TestCase):
    def test_sq_int(self):
        self.assertEqual(sq(2), 4)
    
    def test_sq_float(self):
        self.assertAlmostEqual(sq(2.11), 4.4521)


if __name__ == "__main__":
    unittest.main(verbosity=2)