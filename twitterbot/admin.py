from django.contrib import admin
from .models import TwitterAccountChecked

# Register your models here.
class TwitterAccountCheckedAdmin(admin.ModelAdmin):
    model = TwitterAccountChecked
    list_display = ["screen_name", "prediction"]

admin.site.register(TwitterAccountChecked, TwitterAccountCheckedAdmin)