from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', default=None, blank=True, null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}({self.parent.name})" if self.parent else self.name


class Object(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField(default='You need it!')
    stats = models.TextField(default='Thats so powerfull!')
    #image = models.ImageField(default=None)

    def __str__(self):
        return self.name
