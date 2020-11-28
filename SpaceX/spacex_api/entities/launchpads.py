import requests
import json

from spacex.spacex_api.api import SpaceXApi

class LaunchPads(SpaceXApi):

    def __init__(self):
        super().__init__()
        self.entity_endpoint = 'launchpads'
        pass

    def get_all(self):
        res = requests.get('{}/{}'.format(self.host, self.entity_endpoint))
        return res.json()