from datetime import datetime

class PrimaryContactInfoModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def full_name(self):
        if 'full_name' in self.json_response:
            return self.json_response['full_name']

    @property
    def title(self):
        if 'title' in self.json_response:
            return self.json_response['title']

    @property
    def department(self):
        if 'department' in self.json_response:
            return self.json_response['department']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def extension(self):
        if 'extension' in self.json_response:
            return self.json_response['extension']

    @property
    def fax(self):
        if 'fax' in self.json_response:
            return self.json_response['fax']

    @property
    def mobile(self):
        if 'mobile' in self.json_response:
            return self.json_response['mobile']

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

