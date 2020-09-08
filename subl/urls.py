
from django.urls import path

from . import views

app_name = 'subl'
urlpatterns = [
    # ex: /west/
    path('', views.search, name='search'),
# ex: /west/1/
]