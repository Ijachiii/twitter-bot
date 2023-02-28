from django.db import models

# Create your models here.
class TwitterAccountsCheck(models.Model):
    screen_name = models.CharField(max_length=100)
    prediction = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.screen_name