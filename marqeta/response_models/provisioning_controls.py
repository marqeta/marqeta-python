from datetime import datetime
from marqeta.response_models.manual_entry import ManualEntry
from marqeta.response_models.wallet_provider_card_on_file import WalletProviderCardOnFile
from marqeta.response_models.in_app_provisioning import InAppProvisioning

class ProvisioningControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def manual_entry(self):
        if 'manual_entry' in self.json_response:
            return ManualEntry(self.json_response['manual_entry'])

    @property
    def wallet_provider_card_on_file(self):
        if 'wallet_provider_card_on_file' in self.json_response:
            return WalletProviderCardOnFile(self.json_response['wallet_provider_card_on_file'])

    @property
    def in_app_provisioning(self):
        if 'in_app_provisioning' in self.json_response:
            return InAppProvisioning(self.json_response['in_app_provisioning'])

