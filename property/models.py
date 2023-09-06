from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Property(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    google_map = models.URLField(max_length=400)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("property-detail", kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='temp/property')
    caption = models.CharField(max_length=40)


class Service(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    water_supply = models.BooleanField(default=False)
    power_backup = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    play_ground = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)


class Nearby(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    gym = models.BooleanField(default=False)
    school = models.BooleanField(default=False)
    market = models.BooleanField(_('Market Place'),default=False)
    mall = models.BooleanField(_('Shopping Mall'),default=False)
