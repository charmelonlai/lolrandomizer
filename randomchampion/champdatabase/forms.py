from django.forms import Form, ModelForm
from randomchampion.champdatabase.models import Champion, Role
from django import forms

class ChampionForm(ModelForm):
	class Meta:
		model = Champion

class ChooseChampionForm(forms.Form):
	ROLE_CHOICES = (
		('all','All'),
		('jungler','Jungler'),
		('top','Top'),
		('mid','Mid'),
		('marksman','Marksman'),
		('support','Support')
		)

	role = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ROLE_CHOICES)