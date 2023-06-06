from django.urls import path

from links.views import LinkListView

urlpatterns = [
    path("", LinkListView.as_view(), name="home"),
]
