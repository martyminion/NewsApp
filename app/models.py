class Source:
  '''
  Source class defines the source objects
  '''
  def __init__(self,id,name,description,category):
    self.id = id
    self.name = name
    self.description = description
    self.category = category


class Articles:
  '''
  defines the articles objects
  '''

  def __init__(self,sourcename,author,title,description,image,publishedAt,url):
    self.sourcename = sourcename
    self.author = author
    self.title = title
    self.description = description
    self.image = image
    self.publishedAt = publishedAt
    self.url = url
    
