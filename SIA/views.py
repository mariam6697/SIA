from django.shortcuts import render
from django.http import HttpResponse

def indexindex(request):
    context={}
    return render(request, 'login.html', context)