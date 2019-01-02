from django.db import models
from django.utils import timezone

class Item(models.Model):
    title = models.CharField(max_length=30, default="Item Title")
    TYPE_CHOICES = (
        ('Transportation', 'Transportation'),
        ('Food', 'Food'),
        ('Alcohol', 'Alcohol'),
        ('Cigarettes', 'Cigarettes'),
        ('Electronics', 'Electronics'),
        ('Leisure', 'Leisure'),
        ('Travelling', 'Travelling')
        )
    type = models.CharField(max_length=14, choices=TYPE_CHOICES, default="Transportation")
    amount = models.FloatField()
    location = models.CharField(max_length=30, default="Locale")
    image = models.FileField(upload_to='uploads/')
    comments = models.TextField(default='Thoughts...')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "- " + self.title

