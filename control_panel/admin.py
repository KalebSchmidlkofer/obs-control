from django.contrib import admin
from .models import scene, source
# Register your models here.

class obs_scenes(admin.ModelAdmin):
  list_display = ('name', 'active')
  search_fields = ('name', 'active')
  
# admin.site.register(scene, obs_scenes)

class obs_sources(admin.ModelAdmin):
  list_display = ('type',)
  
admin.site.register(source, obs_sources)