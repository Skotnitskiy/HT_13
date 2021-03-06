from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name_plural = 'Categories'

