import json

from django.http import JsonResponse

from spacex.spacex_api.entities.launchpads import LaunchPads
from spacex.adapters.LaunchPadsAdapter import LaunchPadsAdapter
from spacex.models.LaunchPads import LaunchPads as LaunchPadsModel

def get_launchpads(request):
    data = LaunchPadsAdapter(LaunchPads).all()
    return JsonResponse(data, status=200, safe=False)

def get_database_launchpads(request):
    model = LaunchPadsModel()
    data = model.all()
    return JsonResponse(data, status=200, safe=False)