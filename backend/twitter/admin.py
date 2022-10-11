from django.contrib import admin

from .models import *


class TweetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tweet, TweetAdmin)
