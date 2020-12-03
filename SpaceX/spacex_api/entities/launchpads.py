import json

from spacex.spacex_api.api import SpaceXApi

class LaunchPads(SpaceXApi):

    def __init__(self):
        super().__init__()
        self.entity_endpoint = 'launchpads'
        pass

    def get_all(self):
        res = self.get(self.entity_endpoint)
        data = res.json()
        return data

    def query(self, name=None, status=None):
        body = {
            'query': {},
            'options': {}
        }

        if name:
            body['query']['name'] = name
        elif status:
            body['query']['status'] = status

        res = self.post('{}/query'.format(self.entity_endpoint), body=body)
        data = res.json()

        return data