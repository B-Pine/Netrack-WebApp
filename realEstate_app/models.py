from django.db import models
from django.db.models import ManyToOneRel

# Create your models here
property_type = [
    ('House', 'House'),
    ('Land', 'Land'),
    ('Car', 'Car'),
    ('Other', 'Other'),
]
class Property(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='uploads/', null=False, blank=False)
    type_field = models.CharField(max_length=50, choices=property_type)
    bathrooms = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    size = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    # agent = ManyToOneRel()

