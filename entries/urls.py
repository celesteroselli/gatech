from django.urls import path
from entries import views
from entries.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('create', EntryForm.as_view(), name='create_entry'),
]
