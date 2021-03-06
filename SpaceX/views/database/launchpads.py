import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from spacex.models.LaunchPads import LaunchPads
from spacex.serializers.launchpadserializer import LaunchPadSerializer

logger = logging.getLogger(__name__)

class LaunchPadDatabaseList(APIView):

    def get(self, request, format=None):
        try:
            launchpads = LaunchPads.objects.all()

            # Filtering
            padstatus = request.query_params.get('status', None)
            name = request.query_params.get('name', None)

            if padstatus:
                launchpads = LaunchPads.objects.filter(status=padstatus)
            elif name:
                launchpads = LaunchPads.objects.filter(name=name)

            serializer = LaunchPadSerializer(launchpads, many=True)
            logger.info('Retrieved data for LaunchPads Database: {}'.format(serializer.data))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as exception:
            logger.exception(exception)