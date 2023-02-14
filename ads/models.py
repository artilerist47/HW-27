from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ad(models.Model):
    STATUS = [
        ("False", "Отсутствует"),
        ("True", "В наличии"),
        ("needs verification", "Требуется проверить на наличие")
    ]
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    is_published = models.CharField(max_length=18, choices=STATUS, default="needs verification")

    def __str__(self):
        return self.name