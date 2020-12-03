from spacex.spacex_api.entities.launchpads import LaunchPads
from spacex.models.LaunchPads import LaunchPads as DatabaseLaunchPads

class LaunchPadsAdapter(DatabaseLaunchPads):
    
    def __init__(self, adaptee: LaunchPads):
        self.adaptee = adaptee()
        pass

    def all(self, **kwargs):
        if kwargs['status']:
            data = self.adaptee.query(status=kwargs['status'])
        elif kwargs['name']:
            data = self.adaptee.query(name=kwargs['name'])
        else:
            data = self.adaptee.get_all()

        return data['docs'] if 'docs' in data else data
