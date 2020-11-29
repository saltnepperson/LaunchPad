from django.test import TestCase

from spacex.models.LaunchPads import LaunchPads

class TestLaunchPadsModel(TestCase):

    def test_new_launchpad_create(self):
        launchpad = LaunchPads(name='test launchpad', status='active')

        self.assertEquals(launchpad.name, 'test launchpad')
        self.assertEquals(launchpad.status, 'active')
        self.assertEquals(type(launchpad.id), str)