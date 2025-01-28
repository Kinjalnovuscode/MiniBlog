from django.contrib import admin
from blog import models
# Register your models here.

@admin.register(models.Post) 
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']

admin.site.site_header = "MiniBlog Administration"
admin.site.site_title = "MiniBlog Admin Portal"
admin.site.index_title = "Welcome to MiniBlog Admin"