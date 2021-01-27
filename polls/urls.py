from django.urls import path
from polls.views import ZolnierzList
from . import views

urlpatterns = [
    path('', views.ZolnierzList, name='zolnierze'),
]
