from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)