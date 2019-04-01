from datetime import datetime, date
import json


class MerchantUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        return self.json_response.get('name', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def contact(self):
        return self.json_response.get('contact', None)

    @property
    def contact_email(self):
        return self.json_response.get('contact_email', None)

    @property
    def longitude(self):
        return self.json_response.get('longitude', None)

    @property
    def latitude(self):
        return self.json_response.get('latitude', None)

    @property
    def address1(self):
        return self.json_response.get('address1', None)

    @property
    def address2(self):
        return self.json_response.get('address2', None)

    @property
    def city(self):
        return self.json_response.get('city', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def province(self):
        return self.json_response.get('province', None)

    @property
    def zip(self):
        return self.json_response.get('zip', None)

    @property
    def phone(self):
        return self.json_response.get('phone', None)

    @property
    def country(self):
        return self.json_response.get('country', None)

    @property
    def partial_auth_flag(self):
        return self.json_response.get('partial_auth_flag', None)

    def __repr__(self):
        return '<Marqeta.response_models.merchant_update_model.MerchantUpdateModel>' + self.__str__()
