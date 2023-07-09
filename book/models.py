from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=221)
    file = models.FileField()

    def __str__(self):
        return self.title