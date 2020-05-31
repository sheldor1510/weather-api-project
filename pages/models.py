from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    def _str__(self):
        return self.name
