from django.db import models

# Create your models here.

class Proudct(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=4000, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)