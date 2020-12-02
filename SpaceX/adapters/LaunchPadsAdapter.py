from spacex.spacex_api.entities.launchpads import LaunchPads
from spacex.models.LaunchPads import LaunchPads as DatabaseLaunchPads

class LaunchPadsAdapter(DatabaseLaunchPads):
    
    def __init__(self, adaptee: LaunchPads):
        self.adaptee = adaptee()
        pass

    def all(self) -> dict:
        launchpads = self.adaptee.get_all()
        return launchpads
