from django.db import models

# Create your models here.

class Items(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(null=False)
    desc=models.TextField()
    img=models.ImageField(verbose_name="Add image")

    def __str__(self):
        return self.name
        