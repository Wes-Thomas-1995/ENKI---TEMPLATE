from django.db import models
from django.contrib.auth.models import User



class UserInformation(models.Model):
    USER_TYPE_CHOICES = (
        (0, 'ENKI Ultimate User'),
        (1, 'Administrative Superuser'),
        (2, 'Company Superuser'),
        (3, 'Mid-Level User'),
        (4, 'Junior User'),
    )

    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    email           = models.CharField(max_length=80)
    phone_nbr       = models.CharField(max_length=11, null=True, blank=True)
    firm            = models.CharField(max_length=80)
    #child_company   = models.CharField(max_length=80)
    permission      = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=False, default=0)

    def __str__(self):
        return self.firm

