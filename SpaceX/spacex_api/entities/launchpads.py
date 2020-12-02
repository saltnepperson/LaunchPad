import json

from spacex.spacex_api.api import SpaceXApi

class LaunchPads(SpaceXApi):

    DEFAULT_COLUMNS = ['id','name','status']

    def __init__(self):
        super().__init__()
        self.entity_endpoint = 'launchpads'
        pass

    def get_all(self):
        res = self.get(self.entity_endpoint)
        data = res.json()
        return data