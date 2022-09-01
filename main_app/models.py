from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField(blank_label='(select country')
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('player_detail', kwarg={'pk': self.id})

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
        ('SG', 'Steel guitar'),
    )
    
    brand = models.CharField(max_length=50)
    kind = models.CharField(max_length=2, choices=KIND_CHOICES)
    model = models.CharField(max_length=50)
    string = models.PositiveIntegerField(default=6, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    released = models.BooleanField()
    players = models.ManyToManyField(Player)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gtr_id': self.id})

    def __str__(self):
        return f'{self.brand} - {self.model}'


class Review(models.Model):
    RATING_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )

    date = models.DateField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    review = models.TextField(max_length=300)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guitar} - {self.id}'