from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class Application(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)


    @property
    def program(self):
        return self.json_response.get('program', None)


    @property
    def environment(self):
        return self.json_response.get('environment', None)


    @property
    def program_short_code(self):
        return self.json_response.get('program_short_code', None)


    @property
    def client_api_base_url(self):
        return self.json_response.get('client_api_base_url', None)


    @property
    def assets_url(self):
        return self.json_response.get('assets_url', None)


    @property
    def access_code(self):
        return self.json_response.get('access_code', None)


    def __repr__(self):
         return '<Marqeta.response_models.application.Application>' + self.__str__()
