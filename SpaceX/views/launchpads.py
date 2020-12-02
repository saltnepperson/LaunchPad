import json
import logging

from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from spacex.spacex_api.entities.launchpads import LaunchPads
from spacex.adapters.LaunchPadsAdapter import LaunchPadsAdapter
from spacex.models.LaunchPads import LaunchPads as LaunchPadsModel
from spacex.serializers.launchpadserializer import LaunchPadSerializer

logger = logging.getLogger(__name__)

def get_launchpads(request):
    try:
        data = LaunchPadsAdapter(LaunchPads).all()
        serializer = LaunchPadSerializer(data, many=True)
        logger.info('Retrieved data for LaunchPads API: {}'.format(serializer.data))
        return JsonResponse({"data": serializer.data}, status=200)
    except Exception as exception:
        logger.exception(exception)


def get_database_launchpads(request):
    try:
        launchpads = LaunchPadsModel.objects.all()
        serializer = LaunchPadSerializer(launchpads, many=True) 
        logger.info('Retrieved data for LaunchPads Database: {}'.format(serializer.data))
        return JsonResponse({"data": serializer.data}, status=200)
    except Exception as exception:
        logger.exception(exception)