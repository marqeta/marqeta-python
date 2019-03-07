from marqeta.response_models.fee import Fee


class FeeDetail(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def memo(self):
        if 'memo' in self.response:
            return self.response['memo']

    @property
    def tags(self):
        if 'tags' in self.response:
            return self.response['tags']

    @property
    def transaction_token(self):
        if 'transaction_token' in self.response:
            return self.response['transaction_token']

    @property
    def fee(self):
        if 'fee' in self.response:
            return Fee(self.response['fee'])
