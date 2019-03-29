from datetime import datetime, date
import json


class PrimaryContactInfoModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def full_name(self):
        return self.json_response.get('full_name', None)

    @property
    def title(self):
        return self.json_response.get('title', None)

    @property
    def department(self):
        return self.json_response.get('department', None)

    @property
    def phone(self):
        return self.json_response.get('phone', None)

    @property
    def extension(self):
        return self.json_response.get('extension', None)

    @property
    def fax(self):
        return self.json_response.get('fax', None)

    @property
    def mobile(self):
        return self.json_response.get('mobile', None)

    @property
    def email(self):
        return self.json_response.get('email', None)

    def __repr__(self):
        return '<Marqeta.response_models.primary_contact_info_model.PrimaryContactInfoModel>'
