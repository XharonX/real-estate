from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser,BaseUserManager
# Create your models here.


class City(models.TextChoices):
    yangon = 'ygn', _('Yangon')
    mdy = 'mdy', _('Mandalay')
    pol = 'pol', _('MayMyo')
    bgo = 'bgo', _('Bago')


class User(AbstractUser):
    users = ['admin', 'owner', 'agency', 'client', 'renter', 'advertiser', ]
    USER_TYPE = [(i, _(usr)) for i, usr in enumerate(users)]
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE)
    phone = models.CharField(_("phone"), max_length=12, blank=True)
    address = models.CharField(_('address'), max_length=100, blank=True)
    location = models.CharField(_('location'), max_length=20, choices=City.choices)
    is_owner = models.BooleanField(default=False)
    is_agency = models.BooleanField(default=False)
    is_builder = models.BooleanField(default=False)
    is_renter = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def setattr(self, user_list):
        for user in user_list:
            if self.__getattribute__(f'is_{user}'):
                pass
            self.__setattr__('is_{}'.format(user.lower()), models.BooleanField(default=False))
        # return super().setattr(user_list)


class OwnerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=1)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normailize_email(self.email)

    def create(self, **kwargs):
        kwargs.update({'user_type': 1, 'is_owner': True})
        return super().create(**kwargs)


class Owner(User):
    objects = OwnerManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.username, self.phone


class ClientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=3)

    def create(self, **kwargs):
        kwargs.update({'user_type': 1, 'is_client': True})
        return super().create(**kwargs)


class Client(User):
    objects = ClientManager()

    class Meta:
        proxy = True


class AgencyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=2)

    def create(self, **kwargs):
        kwargs.update({'user_type': 1, 'is_agency': True})
        return super().create(**kwargs)


class Agency(User):
    objects = AgencyManager()

    class Meta:
        proxy = True
