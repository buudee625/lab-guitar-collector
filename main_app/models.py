from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Guitar(models.Model):
        
    KIND_CHOICES = (
        ('AG', 'Acoustic guitar'),
        ('EG', 'Electric guitar'),
        ('MG', 'Multi-string guitar'),
        ('AB', 'Acoustic bass'),
        ('EB', 'Electric bass'),
        ('MB', 'Multi-string bass'),
        ('CG', 'Classical/Nylon guitar'),
        ('AR', 'Archtop/Hollow guitar'),
        ('RE', 'Resonator'),
        ('SG', 'Stell guitar'),
    )
    
    brand = models.CharField(max_length=50)
    kind = models.CharField(max_length=2, choices=KIND_CHOICES)
    model = models.CharField(max_length=50)
    string = models.PositiveIntegerField(default=6, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    released = models.BooleanField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gtr_id': self.id})

    def __str__(self):
        return f'{self.brand} - {self.model}'


class Review(models.Model):
    date = models.DateField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=5, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    review = models.TextField(max_length=300)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guitar} - {self.id}'