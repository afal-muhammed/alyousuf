from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from applications.accounts.models import User
# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class JobOpportunities(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    location = models.CharField(_('Location'), max_length=150)
    job_description = models.TextField(_('Job Description'), null=True, blank=True)
    company_logo = models.FileField(_('Company Logo'), upload_to='Company Logos', null=True, blank=True)
    company_name = models.CharField(_('Company Name'), max_length=150)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title + self.company_name

    def get_job_image(self):
        return self.company_logo.url if self.company_logo else  settings.STATIC_URL + 'images/jobs.jpg'
