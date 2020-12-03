import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from spacex.spacex_api.entities.launchpads import LaunchPads
from spacex.adapters.LaunchPadsAdapter import LaunchPadsAdapter
from spacex.serializers.launchpadserializer import LaunchPadSerializer

logger = logging.getLogger(__name__)

class LaunchPadAPIList(APIView):
    
    def get(self, request, format=None):
        try:
            padstatus = request.query_params.get('status', None)
            name = request.query_params.get('name', None)

            launchpads = LaunchPadsAdapter(LaunchPads).all(status=padstatus, name=name)
            serializer = LaunchPadSerializer(launchpads, many=True)

            logger.info('Retrieved data for LaunchPads API: {}'.format(serializer.data))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as exception:
            logger.exception(exception)
