from django.urls import path
from django.views.generic import TemplateView

from mainapp.views import MainListView, MainCreateView, MainDetailView

app_name = 'mainapp'

urlpatterns = [
    path('list/', MainListView.as_view(), name='list'),
    path('create/', MainCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', MainDetailView.as_view(), name='detail'),
]