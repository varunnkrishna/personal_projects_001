from django.db import models
from datetime import date
from django.utils.translation import gettext as _
import datetime

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(_("Date"), default=datetime.date.today)
    # time = models.DateField(_("Time"), default=datetime.time())

    def __str__(self):
    	return '{} {}'.format(self.email, self.date)