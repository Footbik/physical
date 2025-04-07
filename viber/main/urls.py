from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('pendulum', views.pendulum, name='pendulum'),
    path('pespring', views.pespring, name='pespring'),
    path('trenie', views.trenie, name='trenie'),
    path('brosok', views.brosok, name='brosok'),
    path('kolibel', views.kolibel, name='kolibel'),
    path('error', views.error, name='error')
]