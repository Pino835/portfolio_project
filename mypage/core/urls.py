from django.urls import path
from .views import home, about, projects, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projecs/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]



