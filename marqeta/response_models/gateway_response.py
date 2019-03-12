from marqeta.response_models.jit_program_response import JitProgramResponse

class GatewayResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def code(self):
        if 'code' in self.json_response:
            return self.json_response['code']

    @property
    def data(self):
        if 'data' in self.json_response:
            return JitProgramResponse(self.json_response['data'])

