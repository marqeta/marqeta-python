"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime

class CardholderMetadata(object):

    def __init__(self, response):
        self.response = response

    @property
    def metadata(self):
        if 'metadata' in self.response:
          return self.response['metadata']
        
        


