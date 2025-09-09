from django.db import models

class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    age = models.IntegerField()

    def __str__(self):
        return f"first_name: {self.first_name} _____  last_name: {self.last_name}"