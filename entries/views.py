from django.shortcuts import render
from entries.models import Entry
from django.views.generic.edit import CreateView

class EntryForm(CreateView):
    model = Entry
    fields = ['name', 'school', 'grade', 'email', 'file']
    template_name = 'entry_create.html'

def index(request):
    return render(request, 'index.html', {})