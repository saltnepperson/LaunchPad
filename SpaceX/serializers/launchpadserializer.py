from rest_framework import serializers

from spacex.models.LaunchPads import LaunchPads

class LaunchPadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LaunchPads
        fields = ['id', 'name', 'status']