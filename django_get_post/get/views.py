from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def get(request):
    template = loader.get_template('inputpage.html')
    return HttpResponse(template.render())
