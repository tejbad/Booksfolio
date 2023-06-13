from django.db import models

# Create your models here.
class buyer_data(models.Model):
    year = models.CharField(max_length=10)
    # CharField(max_length=10)
    sem = models.CharField(max_length=10)
    sub = models.CharField(max_length=10)

