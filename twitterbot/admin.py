from django.contrib import admin
from .models import TwitterAccountsCheck

# Register your models here.
class TwitterAccountCheckedAdmin(admin.ModelAdmin):
    model = TwitterAccountsCheck
    list_display = ["screen_name", "prediction"]

admin.site.register(TwitterAccountsCheck, TwitterAccountCheckedAdmin)