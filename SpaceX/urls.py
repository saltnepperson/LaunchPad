from django.urls import path, include

from spacex.views.database.launchpads import LaunchPadDatabaseList
from spacex.views.api.launchpads import LaunchPadAPIList

app_name = 'spacex'

urlpatterns = [
    path('launchpads', LaunchPadAPIList.as_view(), name='get-api-launchpads'),
    path('database/launchpads', LaunchPadDatabaseList.as_view(), name='get-database-launchpads')
]