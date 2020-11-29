from spacex.spacex_api.entities.launchpads import LaunchPads

class LaunchPadsAdapter(LaunchPads):
    
    def __init__(self, adaptee):
        self.adaptee = adaptee()
        pass

    def all(self) -> dict:
        launchpads = self.adaptee.get_all()
        return launchpads
