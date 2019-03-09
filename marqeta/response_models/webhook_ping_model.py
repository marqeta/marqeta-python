from datetime import datetime
from marqeta.response_models.echo_ping_request import EchoPingRequest

class WebhookPingModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def pings(self):
        if 'pings' in self.json_response:
            return [EchoPingRequest(val) for val in self.json_response['pings']]

