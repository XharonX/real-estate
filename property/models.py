from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Property(models.Model):

    class PropertyType(models.IntegerChoices):

        apartment = 0, _("Apartment")
        condo = 1, _('Condo')
        home = 2, _('Home')

        land = 3, _('Land')
        industrial = 4, _('For Industrial')
        field = 5, _("Farm Field")

    class PropertyStatus(models.IntegerChoices):
        listed = 0, _("Listing")
        sold = 1, _('Sold')
        rendering = 2, _('Rendering')

    class City(models.TextChoices):
        yangon = 'ygn', _('Yangon')
        mdy = 'mdy', _('Mandalay')
        pol = 'pol', _('MayMyo')
        bgo = 'bgo', _('Bago')

    #     Here That will be added more state or city

    name = models.CharField(_("name"), max_length=200)
    owner = models.CharField(_('owner'), max_length=50, blank=True)
    type = models.PositiveSmallIntegerField(_('property type'), choices=PropertyType.choices, default=PropertyType.home)
    status = models.PositiveSmallIntegerField(_('status'), choices=PropertyStatus.choices, default=PropertyStatus.listed)
    city = models.CharField(_('city'), max_length=8, choices=City.choices, blank=False, null=True)
    google_map = models.URLField(_('google_map'), max_length=400)
    square_feet = models.CharField(_('square feet'), max_length=10, blank=False)
    price = models.IntegerField()
    bedroom = models.PositiveSmallIntegerField(_('How many do bedroom have?'), default=0)
    bathroom = models.PositiveSmallIntegerField(_('How many do bathroom have?'), default=0)
    address = models.CharField(_('address'), max_length=300)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    # description = models.TextField()
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s - %s', (self.address, self.city)

    def get_absolute_url(self):
        return reverse("property-detail", kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'properties'


class PropertyManager(models.Manager):
    def listed(self):
        qs = super().get_query_set()
        return qs.filter(models.Q(status=Property.PropertyStatus.listed or models.Q(Property.PropertyStatus.rendering)))


class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='temp/property')
    caption = models.CharField(max_length=40)


class Service(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    lift = models.BooleanField(_('lift'), default=False)
    security_guard = models.BooleanField(_('security_guard'), default=False)
    water_supply = models.BooleanField(_('water supply'), default=False)
    power_backup = models.BooleanField(_('power backup'),default=False)
    garden = models.BooleanField(_('garden'), default=False)
    play_ground = models.BooleanField(_('play ground'), default=False)

    def __str__(self):
        return self.property.name[:4] + "'s features"


class Nearby(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    gym = models.BooleanField(_('gym'), default=False)
    school = models.BooleanField(_('school'), default=False)
    market = models.BooleanField(_('Market Place'),default=False)
    mall = models.BooleanField(_('Shopping Mall'),default=False)
    hospital = models.BooleanField(_('hospital'), default=False)
    parking = models.BooleanField(_('parking'), default=False)

    def __str__(self):
        return self.property.name[:4] + "'s nearby buildings"
