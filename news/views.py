from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(" LIMS INDEX. \n my site is alive motherfuckers \m/")