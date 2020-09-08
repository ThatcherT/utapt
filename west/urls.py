
from django.urls import path

from . import views

app_name = 'west'
urlpatterns = [
    # ex: /west/
    path('', views.IndexView.as_view(), name='index'),
# ex: /west/1/
    path("apartments/<int:pk>/", views.DetailView.as_view(), name = 'detail'),
#The DetailView generic view expects the primary key value captured from the URL to be called "pk",
    # so we’ve changed question_id to pk for the generic views.
# ex: /west/1/reviews
    path("<int:pk>/reviews/", views.ReviewsView.as_view(), name = 'reviews'),
    #ex: /west/1/reviewit
    path("<int:apartment_id>/reviewit/", views.reviewit, name = 'reviewit'),
    path('search/', views.search, name='search')
]
