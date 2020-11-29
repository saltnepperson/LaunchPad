from django.urls import path, include

from spacex.views import launchpads

urlpatterns = [
    path('launchpads', launchpads.get_launchpads),
    path('database/launchpads', launchpads.get_database_launchpads)
]