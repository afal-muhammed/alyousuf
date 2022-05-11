from django.db import models
from django.utils.translation import ugettext as _
from applications.accounts.models import User

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class JobOpportunities(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    user_obj = models.ForeignKey(User, null=True, blank=True, related_name='jobs', on_delete=models.CASCADE)
    location = models.CharField(_('Location'), max_length=150)
    posted_date = models.DateTimeField(_('Posted Date'), max_length=150, null=False, blank=False)
    job_description = models.TextField(_('Job Description'), null=True, blank=True)
    company_logo = models.FileField(_('Company Logo'), upload_to='Company Logos', null=True, blank=True)
    slug = models.SlugField(_('Slug'), max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)