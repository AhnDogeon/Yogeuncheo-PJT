from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('score/', views.read_score, name="view_score"),
]