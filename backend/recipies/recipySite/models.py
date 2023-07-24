from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.title.title()}'

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])
    

class Recipy(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField

    def __str__(self):
        return f'{self.title.title()}: {self.description[:100]}'

    def get_absolute_url(self):
        return reverse('recipy', args=[str(self.id)])


    