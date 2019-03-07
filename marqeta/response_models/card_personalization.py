"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime

class CardPersonalization(object):

    def __init__(self, response):
        self.response = response

    @property
    def text(self):
        if 'text' in self.response:
        
            return Text(self.response['text'])
        
    @property
    def images(self):
        if 'images' in self.response:
        
            return Images(self.response['images'])
        
    @property
    def carrier(self):
        if 'carrier' in self.response:
        
            return Carrier(self.response['carrier'])


class Text(object):

    def __init__(self, response):
        self.response = response

    @property
    def name_line_1(self):
        if 'name_line_1' in self.response:
            return TextValue(self.response['name_line_1'])

    @property
    def name_line_2(self):
        if 'name_line_2' in self.response:
            return TextValue(self.response['name_line_2'])


class TextValue(object):

    def __init__(self, response):
        self.response = response

    @property
    def value(self):
        if 'value' in self.response:
            return self.response['value']


class Images(object):

    def __init__(self, response):
        self.response = response

    @property
    def card(self):
        if 'card' in self.response:
            return ImagesCard(self.response['card'])

    @property
    def carrier(self):
        if 'carrier' in self.response:
            return ImagesCarrier(self.response['carrier'])

    @property
    def signature(self):
        if 'signature' in self.response:
            return ImagesSignature(self.response['signature'])

    @property
    def carrier_return_window(self):
        if 'carrier_return_window' in self.response:
            return ImagesCarrierReturnWindow(self.response['carrier_return_window'])


class ImagesCard(object):

    def __init__(self, response):
        self.response = response

    @property
    def name(self):
        if 'name' in self.response:
            return self.response['name']

    @property
    def thermal_color(self):
        if 'thermal_color' in self.response:
            return self.response['thermal_color']


class ImagesCarrier(object):

    def __init__(self, response):
        self.response = response

    @property
    def name(self):
        if 'name' in self.response:
            return self.response['name']

    @property
    def message_1(self):
        if 'message_1' in self.response:
            return self.response['message_1']


class ImagesCarrierReturnWindow(object):

    def __init__(self, response):
        self.response = response

    @property
    def name(self):
        if 'name' in self.response:
            return self.response['name']


class ImagesSignature(object):

    def __init__(self, response):
        self.response = response

    @property
    def name(self):
        if 'name' in self.response:
            return self.response['name']


class Carrier(object):

    def __init__(self, response):
        self.response = response

    @property
    def template_id(self):
        if 'template_id' in self.response:
            return self.response['template_id']

    @property
    def logo_file(self):
        if 'logo_file' in self.response:
            return self.response['logo_file']

    @property
    def logo_thumbnail_file(self):
        if 'logo_thumbnail_file' in self.response:
            return self.response['logo_thumbnail_file']

    @property
    def message_file(self):
        if 'message_file' in self.response:
            return self.response['message_file']

