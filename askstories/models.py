from django.db import models
from main.models import Category


class Askstories(models.Model):
    category = models.ForeignKey(Category, on_delete=False)
    by = models.CharField(max_length=100, blank=True, null=True)
    descendants = models.CharField(max_length=15, blank=True, null=True)
    id = models.TextField(unique=True, primary_key=True, blank=True)
    kids = models.TextField(blank=True, null=True)
    score = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Askstories'
