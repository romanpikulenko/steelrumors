from django.shortcuts import render
from django.views.generic import ListView

from links.models import Link


# Create your views here.
class LinkListView(ListView):
    model = Link
