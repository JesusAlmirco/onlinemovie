from django.contrib import admin
#Import all model
from .models import *

# Register your models here.
class MyMovie(admin.ModelAdmin):
    list_display = ('name', 'description', 'year', 'star', 'show')
    list_filter = ('star', 'show')
    
admin.site.register(Movie, MyMovie)