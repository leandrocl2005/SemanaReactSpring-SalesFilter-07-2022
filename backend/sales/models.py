from django.db import models

# Create your models here.
class Sale(models.Model):
    seller_name = models.CharField(max_length=64)
    visited = models.IntegerField(default=0)
    deals = models.IntegerField(default=0)
    amount = models.FloatField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
