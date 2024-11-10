from django.urls import path
from . import api
from .api import api

urlpatterns = [
   path('api/', api.urls)
]  
