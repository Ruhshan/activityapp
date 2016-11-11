from __future__ import unicode_literals
from django.db import models

class Stream(models.Model):
	value=models.CharField(max_length=200)
	
	def __str__(self):
		return self.value

 