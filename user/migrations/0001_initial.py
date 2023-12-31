# Generated by Django 4.2.1 on 2023-09-09 20:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'owner'), (2, 'agency'), (3, 'builder'), (5, 'client'), (6, 'renter'), (0, 'admin')])),
                ('is_owner', models.BooleanField(default=False)),
                ('is_agency', models.BooleanField(default=False)),
                ('is_builder', models.BooleanField(default=False)),
                ('is_renter', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=12, verbose_name='phone number')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='address')),
                ('location', models.CharField(choices=[('ygn', 'Yangon'), ('mdy', 'Mandalay'), ('pol', 'MayMyo'), ('bgo', 'Bago')], max_length=20, verbose_name='location')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='phone number')),
                ('address', models.CharField(max_length=300, verbose_name='contact address')),
                ('location', models.CharField(choices=[('ygn', 'Yangon'), ('mdy', 'Mandalay'), ('pol', 'MayMyo'), ('bgo', 'Bago')], max_length=20, verbose_name='location')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=12, verbose_name='phone number')),
                ('location', models.CharField(choices=[('ygn', 'Yangon'), ('mdy', 'Mandalay'), ('pol', 'MayMyo'), ('bgo', 'Bago')], max_length=20, verbose_name='location')),
                ('interests', models.ManyToManyField(null=True, to='property.property')),
            ],
        ),
    ]
