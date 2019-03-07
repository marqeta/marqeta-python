from datetime import datetime

class AvsInformation(object):

    def __init__(self, response):
        self.response = response

    @property
    def street_address(self):
        if 'street_address' in self.response:
         
             return self.response['street_address']
            
        
    @property
    def zip(self):
        if 'zip' in self.response:
         
             return self.response['zip']
            
        
    @property
    def postal_code(self):
        if 'postal_code' in self.response:
         
             return self.response['postal_code']
            
        


