from django.db import models


class User(models.Model):
    telegram_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=221, unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=221)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name