from django.urls import path
from django.views.generic import TemplateView

from artistapp.views import ArtistCreateView, ArtistListView, ArtistDetailView

app_name = 'artistapp'

urlpatterns = [
    path('list/', ArtistListView.as_view(), name='list'),
    path('create/', ArtistCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ArtistDetailView.as_view(), name='detail'),
]