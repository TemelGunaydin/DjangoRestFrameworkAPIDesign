from django.db import models

class Todos(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    objects = models.Manager()

    def __str__(self):
        return self.name + '-' + self.description
