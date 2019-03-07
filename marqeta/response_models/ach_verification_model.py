
class AchVerificationModel(object):

    def __init__(self, response):
        self.response = response

    @property
    def verify_amount1(self):
        if 'verify_amount1' in self.response:
            return self.response['verify_amount1']

    @property
    def verify_amount2(self):
        if 'verify_amount2' in self.response:
            return self.response['verify_amount2']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']
