from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateRecord.as_view()),
]