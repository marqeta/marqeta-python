from marqeta.response_models.card_personalization import CardPersonalization


class CardFulfillmentResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def shipping(self):
        if 'shipping' in self.response:
            return ShippingInformationResponse(self.response['shipping'])

    @property
    def card_personalization(self):
        if 'card_personalization' in self.response:
            return CardPersonalization(self.response['card_personalization'])


class ShippingInformationResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def method(self):
        if 'method' in self.response:
            return self.response['method']

    @property
    def return_address(self):
        if 'return_address' in self.response:
            return FulfillmentAddressResponse(self.response['return_address'])

    @property
    def recipient_address(self):
        if 'recipient_address' in self.response:
            return FulfillmentAddressResponse(self.response['recipient_address'])

    @property
    def care_of_line(self):
        if 'care_of_line' in self.response:
            return self.response['care_of_line']


class FulfillmentAddressResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def first_name(self):
        if 'first_name' in self.response:
            return self.response['first_name']

    @property
    def middle_name(self):
        if 'middle_name' in self.response:
            return self.response['middle_name']

    @property
    def last_name(self):
        if 'last_name' in self.response:
            return self.response['last_name']

    @property
    def address1(self):
        if 'address1' in self.response:
            return self.response['address1']

    @property
    def address2(self):
        if 'address2' in self.response:
            return self.response['address2']

    @property
    def city(self):
        if 'city' in self.response:
            return self.response['city']

    @property
    def state(self):
        if 'state' in self.response:
            return self.response['state']

    @property
    def zip(self):
        if 'zip' in self.response:
            return self.response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.response:
            return self.response['postal_code']

    @property
    def country(self):
        if 'country' in self.response:
            return self.response['country']

    @property
    def phone(self):
        if 'phone' in self.response:
            return self.response['phone']






