from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def bn(reguest):
    return HttpResponse('Hello! Its my project')

def bm(reguest):
    return HttpResponse(datetime)

def bi(reguest):
    return HttpResponse('Goodby user!')

print('commit')



