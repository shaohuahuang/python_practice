import unittest

from main import unnecessary_math


class TestUM(unittest.TestCase):
  def setUp(self):
    pass

  def test_number_3_4(self):
    self.assertEqual(unnecessary_math.multiply(3, 4), 12)

if __name__ == '__main__':
  unittest.main()
