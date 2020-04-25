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

  def __init__(self,author,title,descriptions,publishedAt,url,content):
    self.author = author
    self.title = title
    self.descriptions = descriptions
    self.publishedAt = publishedAt
    self.url = url
    self.content = content
    
