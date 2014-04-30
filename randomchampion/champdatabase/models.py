from django.db import models
from django.shortcuts import get_object_or_404
import random

class Role(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Champion(models.Model):
	name = models.CharField(max_length = 30)
	title = models.CharField(max_length = 50)
	splash = models.ImageField('splash art', upload_to="splash/",blank = True, null = True)
	role = models.ManyToManyField(Role)

	def __unicode__(self):
		return self.name


	@staticmethod
	def get_random(role=None):
		if role == None:
			final_list = Champion.objects.all()
		else:
			r = get_object_or_404(Role, name=role)
			final_list = r.champion_set.all()
		return random.choice(final_list)
