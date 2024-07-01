from django.urls import path
from . import views


urlpatterns = [
    path('', views.one, name='1'),
    path('admin', views.admin, name='2'),
]