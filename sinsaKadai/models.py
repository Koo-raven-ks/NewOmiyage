from django.db import models

# Create your models here.


class Omiyage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="omiyage_images/", blank=True, null=True)
    taste = models.CharField(max_length=100, default="とんこつラーメン味")

    def __str__(self):
        return self.name
