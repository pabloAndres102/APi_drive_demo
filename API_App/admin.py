from django.contrib import admin
from API_App.models import Post
# Register your models here.


@admin.register(Post)
class post_admin(admin.ModelAdmin):
    list_display = ['id','title']