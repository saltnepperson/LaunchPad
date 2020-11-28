import requests

class SpaceXApi():

    PROTOCOL = 'https'
    BASE_URL = 'api.spacexdata.com'
    API_VERSION = 'v4'

    def __init__(self):
        self.host = '{}://{}/{}'.format(self.PROTOCOL, self.BASE_URL, self.API_VERSION)
        pass
