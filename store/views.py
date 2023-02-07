from django.shortcuts import render
from .models import Clothes
from django.views.generic import ListView, DetailView

# Create your views here.
class HomePage(ListView):
    model = Clothes
    template_name = 'store/home.html'
    context_object_name = 'clothes'

class DetailPage(DetailView):
    model = Clothes
    template_name = 'store/detail.html'
    context_object_name = 'clothes'