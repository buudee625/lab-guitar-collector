from django.db import models
from django.urls import reverse

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
    string = models.IntegerField(default=6)
    released = models.BooleanField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gtr_id': self.id})

    def __str__(self):
        return f'{self.brand} - {self.model}'
