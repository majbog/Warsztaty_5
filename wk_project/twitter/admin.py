from django.contrib import admin

from .models import Message, Following, Comment

# Register your models here.

# admin.site.register(User)
admin.site.register(Message)
admin.site.register(Following)
admin.site.register(Comment)

