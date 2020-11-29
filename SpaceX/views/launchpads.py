import json
import logging

from django.http import JsonResponse

from spacex.spacex_api.entities.launchpads import LaunchPads
from spacex.adapters.LaunchPadsAdapter import LaunchPadsAdapter
from spacex.models.LaunchPads import LaunchPads as LaunchPadsModel

logger = logging.getLogger(__name__)

def get_launchpads(request):
    try:
        data = LaunchPadsAdapter(LaunchPads).all()
        return JsonResponse({"data": data}, status=200)
    except Exception as exception:
        logger.exception(exception)


def get_database_launchpads(request):
    try:
        model = LaunchPadsModel()
        data = model.all()
        return JsonResponse({"data": data}, status=200)
    except Exception as exception:
        logger.exception(exception)