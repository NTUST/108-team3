from django.shortcuts import render_to_response
from django.shortcuts import render
from .models import Photo,Group,Quiz

# Create your views here.
def index(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/index.html", context)

def the_news(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/最新消息.html", context)

def about_us(request):
	groups = Group.objects.all()
	return render_to_response('html/關於我們.html',locals())

def item_bank(request):
	return render_to_response('html/題庫.html',locals())

def simulation_prob(request):
	return render_to_response('html/模擬題.html',locals())

def quiz_BTS(request):
	queryset = Quiz.objects.all().filter(vid=1)
	context = {
		"quizs": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/quiz_BTS.html", context)

def quiz_GOT7(request):
	queryset = Quiz.objects.all().filter(vid=3)
	context = {
		"quizs": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/quiz_GOT7.html", context)

def quiz_seventeen(request):
	queryset = Quiz.objects.all().filter(vid=4)
	context = {
		"quizs": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/quiz_seventeen.html", context)

def quiz_TWICE(request):
	queryset = Quiz.objects.all().filter(vid=6)
	context = {
		"quizs": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/quiz_TWICE.html", context)

def quiz_SJ(request):
	queryset = Quiz.objects.all().filter(vid=5)
	context = {
		"quizs": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/quiz_SJ.html", context)

def quiz_EXO(request):
	queryset = Quiz.objects.all().filter(vid=2)
	context = {
		"quizs": queryset,
		"groups": Group.objects.all(),
	}
	return render(request, "html/quiz_EXO.html", context)

def itembank_BTS(request):
	groups = Group.objects.all()
	Subject = Group.objects.get(vid='bts')
	return render_to_response('html/itembank_BTS.html',locals())

def itembank_SJ(request):
	groups = Group.objects.all()
	Subject = Group.objects.get(vid='sj')
	return render_to_response('html/itembank_SJ.html',locals())

def itembank_EXO(request):
	groups = Group.objects.all()
	Subject = Group.objects.get(vid='exo')
	return render_to_response('html/itembank_EXO.html',locals())

def itembank_TWICE(request):
	groups = Group.objects.all()
	Subject = Group.objects.get(vid='twice')
	return render_to_response('html/itembank_TWICE.html',locals())

def itembank_GOT7(request):
	groups = Group.objects.all()
	Subject = Group.objects.get(vid='got7')
	return render_to_response('html/itembank_GOT7.html',locals())
	
def itembank_seventeen(request):
	groups = Group.objects.all()
	Subject = Group.objects.get(vid='svt')
	return render_to_response('html/itembank_seventeen.html',locals())
