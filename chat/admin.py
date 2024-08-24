from .models import Chat, Message
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text', 'created_at', 'author', 'reciver')
    list_display = ('text', 'created_at', 'author', 'reciver')
    search_fields = ('text', 'author', 'reciver')

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
