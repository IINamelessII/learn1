from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}({self.parent.name})"


class Object(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField(default='You need it!')
    stats = models.TextField(default='Thats so powerfull!')

    def __str__(self):
        return f"{self.name} ({self.category.name})"
