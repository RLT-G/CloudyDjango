from django.urls import path
from . import views

urlpatterns = [
    path('destiny/', view=views.index, name="lending")
]
