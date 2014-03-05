from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context


def index(request):
	return render(request,"index.html")