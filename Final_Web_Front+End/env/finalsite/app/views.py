from django.shortcuts import render_to_response
from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
	}
	return render(request, "html/index.html", context)

def the_news(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
	}
	return render(request, "html/最新消息.html", context)

def about_us(request):
	return render_to_response('html/關於我們.html',locals())

def item_bank(request):
	return render_to_response('html/題庫.html',locals())

def simulation_prob(request):
	return render_to_response('html/模擬題.html',locals())

def quiz_BTS(request):
	return render_to_response('html/quiz_BTS.html',locals())

def quiz_GOT7(request):
	return render_to_response('html/quiz_GOT7.html',locals())

def quiz_seventeen(request):
	return render_to_response('html/quiz_seventeen.html',locals())

def quiz_TWICE(request):
	return render_to_response('html/quiz_TWICE.html',locals())

def quiz_SJ(request):
	return render_to_response('html/quiz_SJ.html',locals())

def quiz_EXO(request):
	return render_to_response('html/quiz_EXO.html',locals())

def itembank_BTS(request):
	return render_to_response('html/itembank_BTS.html',locals())
def itembank_SJ(request):
	return render_to_response('html/itembank_SJ.html',locals())
def itembank_EXO(request):
	return render_to_response('html/itembank_EXO.html',locals())
def itembank_TWICE(request):
	return render_to_response('html/itembank_TWICE.html',locals())
def itembank_GOT7(request):
	return render_to_response('html/itembank_GOT7.html',locals())
def itembank_seventeen(request):
	return render_to_response('html/itembank_seventeen.html',locals())
