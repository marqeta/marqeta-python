from datetime import datetime
from marqeta.response_models.provisioning_controls import ProvisioningControls

class DigitalWalletTokenization(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def provisioning_controls(self):
        if 'provisioning_controls' in self.json_response:
            return ProvisioningControls(self.json_response['provisioning_controls'])

