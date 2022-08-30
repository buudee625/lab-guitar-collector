from django.db import models
from django.urls import reverse

# Create your models here.
class Guitar(models.Model):
        
    KIND_CHOICES = (
        ('1', 'Acoustic guitar'),
        ('2', 'Electric guitar'),
        ('3', 'Acoustic bass'),
        ('4', 'Electric bass'),
    )
    
    brand = models.CharField(max_length=50)
    kind = models.CharField(max_length=2, choices=KIND_CHOICES)
    model = models.CharField(max_length=50)
    string = models.IntegerField(default=6)
    released = models.BooleanField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gtr_id': self.id})
