from django.contrib import admin
from entries.models import *

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, PostAdmin)
