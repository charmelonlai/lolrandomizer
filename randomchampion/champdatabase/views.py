from django.shortcuts import render
from randomchampion.champdatabase.models import Champion, Role
from django.views.generic import TemplateView
from randomchampion.champdatabase.forms import ChooseChampionForm

# Create your views here.

class FrontPageView(TemplateView):

	template_name = 'index.html'
	
	def post(self, request, *args, **kwargs):
		form = ChooseChampionForm(request.POST)
		champion = Champion.get_random()
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)

	def post1(self, request, *args, **kwargs):
		form = ChooseChampionForm(request.POST)
		champion = Champion.get_random('Jungler')
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)