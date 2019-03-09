from marqeta.response_models.card_personalization import CardPersonalization


class CardFulfillmentResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def shipping(self):
        if 'shipping' in self.json_response:
            return ShippingInformationResponse(self.json_response['shipping'])

    @property
    def card_personalization(self):
        if 'card_personalization' in self.json_response:
            return CardPersonalization(self.json_response['card_personalization'])


class ShippingInformationResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def method(self):
        if 'method' in self.json_response:
            return self.json_response['method']

    @property
    def return_address(self):
        if 'return_address' in self.json_response:
            return FulfillmentAddressResponse(self.json_response['return_address'])

    @property
    def recipient_address(self):
        if 'recipient_address' in self.json_response:
            return FulfillmentAddressResponse(self.json_response['recipient_address'])

    @property
    def care_of_line(self):
        if 'care_of_line' in self.json_response:
            return self.json_response['care_of_line']


class FulfillmentAddressResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def first_name(self):
        if 'first_name' in self.json_response:
            return self.json_response['first_name']

    @property
    def middle_name(self):
        if 'middle_name' in self.json_response:
            return self.json_response['middle_name']

    @property
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def address1(self):
        if 'address1' in self.json_response:
            return self.json_response['address1']

    @property
    def address2(self):
        if 'address2' in self.json_response:
            return self.json_response['address2']

    @property
    def city(self):
        if 'city' in self.json_response:
            return self.json_response['city']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']






