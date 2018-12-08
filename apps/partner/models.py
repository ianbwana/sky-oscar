from django.db import models

from oscar.apps.partner.abstract_models import AbstractPartner
from phonenumber_field.modelfields import PhoneNumberField


class Partner(AbstractPartner):
    email = models.EmailField(null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = PhoneNumberField(null=True)

from oscar.apps.partner.models import *  # noqa isort:skip