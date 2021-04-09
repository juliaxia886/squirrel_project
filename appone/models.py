from django.db import models
from django.utils.translation import gettext as _

class Pet(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=_('Name of pet'),
    )

    breed = models.CharField(
        max_length=100,
        help_text=_('Breed of pet'),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    SEX_CHOICES = [
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (OTHER, _('Other')),
    ]

    sex = models.CharField(
        max_length=15,
        help_text=_('Sex of pet'),
        choices=SEX_CHOICES,
        default=OTHER,
    )

    birth_date = models.DateField(
        help_text=_('Birth date of pet'),
    )

    vaccinated = models.BooleanField(
        help_text=_('Whether or not pet is vaccinated'),
    )

    profile_image = models.ImageField(
        help_text=_('Profile picture of pet'),
        blank=True,
        upload_to='profiles_images',
    )

    bio = models.TextField(
            blank=True,
    )
            
