from django.shortcuts import render

# Create your views here.
from .forms import RegistrationForm

def home(request):
	form = RegistrationForm()
	context = {"form":form}
	template = "home2.html"
	return render(request, template, context)


def angOne(request):
	context = {}
	template = "angStart.html"
	return render(request, template, context)