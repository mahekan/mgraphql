
from string import Template
import requests
# A simple function to use requests.post to make the API call. Note the json= section.
class Mgraphql:
  def __init__(self,url,token = None):
    self.url = url
    self.token = token
  def query(self,query,): 
    self.query = query
    print (self.token)
    self.headers = {'Authorization':self.token}
    self.request = requests.post(self.url, json={'query': self.query},headers = self.headers)
    if self.request.status_code == 200:
        return self.request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(self.request.status_code, self.query))
        
    
  def mutation(self,query,variables,): 
    self.queryTemplate = Template(query)
    print(self.queryTemplate)
    self.query = self.queryTemplate.substitute(variables)
    self.headers = {'Authorization':self.token}
    self.request = requests.post(self.url, json={'query': self.query},headers = self.headers)
    if self.request.status_code == 200:
        return self.request.json()
    else:
        raise Exception("mutation failed to run by returning code of {}. {}".format(self.request.status_code, self.query))
  