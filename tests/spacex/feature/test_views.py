from django.test import TestCase
from django.urls import reverse

class TestLaunchPadsView(TestCase):

    def test_context(self):
        response = self.client.get(reverse('get-api-launchpads'))
        self.assertGreater(len(response.context), 0)