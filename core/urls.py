from django.urls import path
from . import views

urlpatterns = [
    path('', views.funds_collection, name='funds_collection'),
]