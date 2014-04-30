from django.shortcuts import render
from randomchampion.champdatabase.models import Champion, Role
from django.views.generic import TemplateView
from randomchampion.champdatabase.forms import ChooseChampionForm

# Create your views here.

class FrontPageView(TemplateView):

	template_name = 'index.html'

	def post(self, request):
		champion = Champion.get_random()
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)

class AllView(TemplateView):

	template_name = 'index.html'

	def post(self, request):
		champion = Champion.get_random()
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)

class JungleView(TemplateView):

	template_name = 'index.html'

	def post(self, request):
		champion = Champion.get_random('Jungler')
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)

class TopView(TemplateView):

	template_name = 'index.html'

	def post(self, request):
		champion = Champion.get_random('Top')
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)

class MidView(TemplateView):

	template_name = 'index.html'

	def post(self, request):
		champion = Champion.get_random('Mid')
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)

class ADView(TemplateView):

	template_name = 'index.html'

	def post(self, request):
		champion = Champion.get_random('Marksman')
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)

class SupportView(TemplateView):

	template_name = 'index.html'

	def post(self, request):
		champion = Champion.get_random('Support')
		context = {}
		context['champion'] = champion
		return render(request,'champ.html',context)