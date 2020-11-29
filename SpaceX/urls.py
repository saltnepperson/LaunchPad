from django.urls import path, include

from spacex.views import launchpads

app_name = 'spacex'

urlpatterns = [
    path('launchpads', launchpads.get_launchpads, name='get-api-launchpads'),
    path('database/launchpads', launchpads.get_database_launchpads, name='get-database-launchpads')
]