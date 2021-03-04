# Euclid's algorithm for finding greatest common divisor
import unittest

class TestGCD(unittest.TestCase):

    def gcd(self, m: int, n: int) -> int:
      if n > m:
        m, n = n, m

      r = m % n
      while r != 0:
        m, n = n, r
        r = m % n
      return n

    def test_gcd(self):
        self.assertEqual(self.gcd(119, 544), 17, "Should be 17")


if __name__ == '__main__':
    unittest.main()
