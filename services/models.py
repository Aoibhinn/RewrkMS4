from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

PLAN_CHOICES = (
    ('B', 'basic'),
    ('S', 'standard'),
    ('P', 'premium')
)

class Service(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    service_title = models.CharField(max_length=250)
    service_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    plan = models.CharField(choices=PLAN_CHOICES, max_length=1)
    is_published = models.BooleanField(default=True)
    slug_service = models.SlugField(max_length=200, unique=True, null=True)


    def __str__(self):
        return self.service_title