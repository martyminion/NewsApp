import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
  '''
  Tests for the Source class
  '''

  def setUp(self):
    '''
    method that runs before each test case
    '''
    self.new_source = Source("bbc-news","bbc news","Some Americans can resume going to restaurants","general")
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Source))

  def test_init(self):
    '''
    test to check if the class is instantiated correctly
    '''
    self.assertEqual(self.new_source.id,"bbc-news")
    self.assertEqual(self.new_source.name,"bbc news")
    self.assertEqual(self.new_source.description,"Some Americans can resume going to restaurants")
    self.assertEqual(self.new_source.category,"general")