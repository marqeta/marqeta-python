
class Address(object):

    def __init__(self, response):
        self.response = response

    @property
    def address1(self):
        return self.response['address1']

    @property
    def address2(self):
        return self.response['address2']

    @property
    def state(self):
        return self.response['state']

    @property
    def city(self):
        return self.response['city']

    @property
    def country(self):
        return self.response['country']

    @property
    def postal_code(self):
        return self.response['postal_code']