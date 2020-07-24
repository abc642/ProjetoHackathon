from django.urls import path
from .views import home, aboutus

urlpatterns = [
    path('',home,name='home'),
    path('about/',aboutus,name='about')
]