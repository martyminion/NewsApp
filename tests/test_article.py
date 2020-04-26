import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
  '''
  Tests for the Articles class
  '''

  def setUp(self):
    '''
    method that runs before each test case
    '''
    self.new_article = Articles("Beth","New Quiz","Some Americans can resume going to restaurants","24/2/2020","bbc-news.com","we cant wait")
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))

  def test_init(self):
    '''
    test to check if the class is instantiated correctly
    '''
    self.assertEqual(self.new_article.author,"Beth")
    self.assertEqual(self.new_article.title,"New Quiz")
    self.assertEqual(self.new_article.descriptions,"Some Americans can resume going to restaurants")
    self.assertEqual(self.new_article.publishedAt,"24/2/2020")
    self.assertEqual(self.new_article.url,"bbc-news.com")
    self.assertEqual(self.new_article.content,"we cant wait")
    