
from string import Template
import requests
import json
# A simple function to use requests.post to make the API call. Note the json= section.
class Mgraphql:
  def __init__(self,url,token = None):
    self.url = url
    self.token = token
  def _req(self,query):
    headers = {'Authorization':self.token}
    request = requests.post(self.url, json={'query': query},headers = headers)
    return request
  def query(self,query,variables=None):
    if variables:
      queryTemplate = Template(query)
      query = queryTemplate.substitute(variables)
    request = self._req(query)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(request.text)
        
    
  def mutation(self,query,variables,): 
    queryTemplate = Template(query)
    query = queryTemplate.substitute(variables)
    request = self._req(query)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(request.text)