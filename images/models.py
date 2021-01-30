from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import uuid

# Create your models here.

def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

OPTIONS = (
        ('active', _('Active')),
        ('deactivated', _('Deactivated'))
    )

class Image(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    alt = models.TextField(null=True) #Alternate text
    image = models.ImageField(
        upload_to=user_directory_path, default='posts/default.jpg'
    )
    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=11, choices=OPTIONS, default='active')