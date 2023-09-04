from django.contrib import admin
from .models import *
# Register your models here

class BlogCreateAdmin (admin.ModelAdmin):
    list_display = ['title', 'category']
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogCreate, BlogCreateAdmin)
admin.site.register(Med)
admin.site.register(Genre)
admin.site.register(Like)
admin.site.register(Comment)