from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class me(models.Model):
	name = models.CharField(max_length=200, null=False)

	def __str__(self):
		return self.name