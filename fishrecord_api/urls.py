from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateRecord.as_view(), name="create"),
    path('records', GetRecord.as_view(), name="records"),
]