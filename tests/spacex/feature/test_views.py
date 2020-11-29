from django.test import TestCase
from django.urls import reverse

class TestLaunchPadsView(TestCase):

    def setUp(self):
        pass

    def test_get_launchpad_data_from_spacex_api(self):
        response = self.client.get(reverse('spacex:get-api-launchpads'))
        self.assertEqual(response.status_code, 200)
        # Cannot assert against hard-coded values since we'll have no idea what the 
        # values are going to be, instead check that there is data
        self.assertGreater(len(response.json()['data']), 0)

    def test_get_launchpad_data_from_model(self):
        response = self.client.get(reverse('spacex:get-database-launchpads'))
        self.assertEqual(response.status_code, 200)