from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
import accounts.models
# Create your models here.
class Blog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	title = models.CharField(max_length = 250)
	body = models.TextField()
	show = models.BooleanField(default=True)

	def __str__(self):
		return self.body

