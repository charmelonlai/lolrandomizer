from django import template
from randomchampion.champdatabase.models import Champion, Role

register = template.Library()

@register.filter(name='getrandom')
def getrandom(role):
	c = Champion.get_random(role)
	return c