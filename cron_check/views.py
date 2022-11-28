from django.http import HttpResponse
from django.shortcuts import render
from weather.models import weather

def index(request):
    dataWeather = weather.objects.all().order_by('-id')[:20]
    data={
        'dataWeather' : dataWeather,
        'title' : 'Index Page'
    }
    return render(request,'index.html',data)

def data(request, id):
    dataWeather = weather.objects.get(id=id)
    data={
        'dataWeather' : dataWeather,
        'title' : "Data Page"
    }
    return render(request,'data.html',data)