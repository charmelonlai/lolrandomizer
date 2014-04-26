from django.db import models
import random

class Role(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Champion(models.Model):
	name = models.CharField(max_length = 30)
	title = models.CharField(max_length = 50)
	role = models.ManyToManyField(Role)

	def __unicode__(self):
		return self.name


	@staticmethod
	def get_random(role=None):
		if role == None:
			final_list = Champion.objects.all()
		else:
			r = Role.objects.get(name=role)
			final_list = r.champion_set.all()
		return random.choice(final_list)
