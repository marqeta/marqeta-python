
class AchVerificationModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def verify_amount1(self):
        if 'verify_amount1' in self.json_response:
            return self.json_response['verify_amount1']

    @property
    def verify_amount2(self):
        if 'verify_amount2' in self.json_response:
            return self.json_response['verify_amount2']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

