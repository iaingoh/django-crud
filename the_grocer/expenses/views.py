from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
                                ListView, 
                                DetailView, 
                                UpdateView,
                                DeleteView)
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Item


class IndexView(ListView):
    template_name = 'expenses/index.html'

    def get_queryset(self):
        return Item.objects.all()

class ItemCreate(CreateView):
    model = Item
    fields = ['title', 'type', 'amount', 'location', 'image', 'comments', 'date']
    success_url = "/expenses/success/"

class ItemUpdate(UpdateView):
    model = Item
    fields = ['title', 'type', 'amount', 'location', 'image', 'comments', 'date']
    success_url = "/expenses/success/"

def success(request):
    return HttpResponse("<h2>Success!</h2><br><a href='/expenses/index/'><button type='button'>Go back to Index</button></a>")

class ItemDetail(DetailView):
    model = Item
    template_name = 'expenses/detail.html'

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('expenses:index')

