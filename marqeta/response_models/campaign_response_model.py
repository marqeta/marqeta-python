from datetime import datetime, date
import json


class CampaignResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def active(self):

        return self.json_response.get('active', None)

    @property
    def name(self):

        return self.json_response.get('name', None)

    @property
    def start_date(self):

        if 'start_date' in self.json_response:
            return datetime.strptime(self.json_response['start_date'], '%Y-%m-%d').date()

    @property
    def end_date(self):

        if 'end_date' in self.json_response:
            return datetime.strptime(self.json_response['end_date'], '%Y-%m-%d').date()

    @property
    def token(self):

        return self.json_response.get('token', None)

    @property
    def store_tokens(self):

        return self.json_response.get('store_tokens', None)

    @property
    def created_time(self):

        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):

        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.campaign_response_model.CampaignResponseModel>'
