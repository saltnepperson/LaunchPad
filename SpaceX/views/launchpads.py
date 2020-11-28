import json

from django.http import JsonResponse

from spacex.spacex_api.entities.launchpads import LaunchPads
from spacex.adapters.LaunchPadsAdapter import LaunchPadsAdapter

def get_launchpads(request):
    data = LaunchPadsAdapter(LaunchPads).all()
    data = json.dumps(data)
    return JsonResponse(data, status=200, safe=False)