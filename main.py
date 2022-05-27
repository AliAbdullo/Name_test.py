import unittest
from misol import katta_son

class Javob(unittest.TestCase):
  def katta(self):
    son = katta_son(7,6,9)
    self.assertAlmostEqual(son,9)

unittest.main()