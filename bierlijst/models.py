from django.db import models

# Create your models here.


class User(models.Model):
    beers = models.IntegerField(default=0)
    returned_crates = models.IntegerField(default=0)


