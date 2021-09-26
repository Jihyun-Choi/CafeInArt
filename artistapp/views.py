from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from artistapp.forms import ArtistCreationForm
from artistapp.models import Artist

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artist_list'
    template_name = 'artistapp/list.html'


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistCreationForm
    template_name = 'artistapp/create.html'

    def get_success_url(self):
        return reverse('artistapp:list')


class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'target_artist'
    template_name = 'artistapp/detail.html'