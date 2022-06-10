from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class ImagesCarrier(object):
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
        return self.json_response.get("name", None)

    @property
    def message_1(self):
        return self.json_response.get("message_1", None)

    def __repr__(self):
        return "<Marqeta.response_models.images_carrier.ImagesCarrier>" + self.__str__()
