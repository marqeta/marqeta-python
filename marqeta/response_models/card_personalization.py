class CardPersonalization(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def text(self):
        if 'text' in self.json_response:
            return Text(self.json_response['text'])

    @property
    def images(self):
        if 'images' in self.json_response:
            return Images(self.json_response['images'])

    @property
    def carrier(self):
        if 'carrier' in self.json_response:
        
            return Carrier(self.json_response['carrier'])


class Text(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name_line_1(self):
        if 'name_line_1' in self.json_response:
            return TextValue(self.json_response['name_line_1'])

    @property
    def name_line_2(self):
        if 'name_line_2' in self.json_response:
            return TextValue(self.json_response['name_line_2'])


class TextValue(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']


class Images(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def card(self):
        if 'card' in self.json_response:
            return ImagesCard(self.json_response['card'])

    @property
    def carrier(self):
        if 'carrier' in self.json_response:
            return ImagesCarrier(self.json_response['carrier'])

    @property
    def signature(self):
        if 'signature' in self.json_response:
            return ImagesSignature(self.json_response['signature'])

    @property
    def carrier_return_window(self):
        if 'carrier_return_window' in self.json_response:
            return ImagesCarrierReturnWindow(self.json_response['carrier_return_window'])


class ImagesCard(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def thermal_color(self):
        if 'thermal_color' in self.json_response:
            return self.json_response['thermal_color']


class ImagesCarrier(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def message_1(self):
        if 'message_1' in self.json_response:
            return self.json_response['message_1']


class ImagesCarrierReturnWindow(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']


class ImagesSignature(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']


class Carrier(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def template_id(self):
        if 'template_id' in self.json_response:
            return self.json_response['template_id']

    @property
    def logo_file(self):
        if 'logo_file' in self.json_response:
            return self.json_response['logo_file']

    @property
    def logo_thumbnail_file(self):
        if 'logo_thumbnail_file' in self.json_response:
            return self.json_response['logo_thumbnail_file']

    @property
    def message_file(self):
        if 'message_file' in self.json_response:
            return self.json_response['message_file']

