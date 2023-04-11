from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Smartphone(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, name="Brand", on_delete=models.CASCADE)
    price = models.IntegerField(default=None)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.model
