import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
  def test_toliq_ism(self):
    formatted_name = get_full_name('ali','valiyev')
    self.assertEqual(formatted_name, 'Ali Valiyev')

  def test_toliq_ism_otasi(self):
    name=get_full_name('hasan','husanov','olimogli')
    self.assertEqual(name,'Hasan Olimogli Husanov')
    
unittest.main()