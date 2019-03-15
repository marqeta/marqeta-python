from datetime import datetime, date
import json

class PrimaryContactInfoModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'full_name' : self.full_name,
           'title' : self.title,
           'department' : self.department,
           'phone' : self.phone,
           'extension' : self.extension,
           'fax' : self.fax,
           'mobile' : self.mobile,
           'email' : self.email,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.primary_contact_info_model.PrimaryContactInfoModel>'