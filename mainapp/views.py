from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from mainapp.forms import GalleryCafeCreationForm
from mainapp.models import GalleryCafe


class MainListView(ListView):
    model = GalleryCafe
    context_object_name = 'main_list'
    template_name = 'mainapp/list.html'

class MainCreateView(CreateView):
    model = GalleryCafe
    form_class = GalleryCafeCreationForm
    template_name = 'mainapp/create.html'

    # 추후 계정생성시 카페주인아이디를 이걸로 저장.....해야돼
    # def form_valid(self, form):
    #     temp_article = form.save(commit=False)
    #     temp_article.writer = self.request.user
    #     temp_article.save()
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('mainapp:list')

class MainDetailView(DetailView):
    model = GalleryCafe
    context_object_name = 'target_gallerycafe'
    template_name = 'mainapp/detail.html'