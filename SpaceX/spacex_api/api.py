import requests

class SpaceXApi():

    PROTOCOL = 'https'
    BASE_URL = 'api.spacexdata.com'
    API_VERSION = 'v4'

    def __init__(self):
        self.host = '{}://{}/{}'.format(self.PROTOCOL, self.BASE_URL, self.API_VERSION)
        self.body = {}
        pass

    # GET wrapper
    def get(self, endpoint):
        return requests.get('{}/{}'.format(self.host, endpoint))

      # POST wrapper
    def post(self, endpoint, body=None):
        if body:
            self.body = body

        return requests.post(
            '{}/{}'.format(self.host, endpoint), 
            json=self.body
            )