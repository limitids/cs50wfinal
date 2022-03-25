from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Resturaunt, zipToCoord
import time
import json
from django.db.models import Count, F, Value

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
currentCoords = [0,0]


def populateZips():
    data = []
    file = open('/Users/thomasbradford/Desktop/scalabilityandsecurity/leaf/ziptocoord.txt')
    for line in file:
        line = line.replace('\n','')
        data = line.split(',')
        obj = zipToCoord.objects.create(zip=data[0],long=data[1],lat=data[2])
        print(obj)
    



def index(request):
    return render(request,"leaf/start.html")

@csrf_exempt
def zipConversion(request):
    if request.method == 'GET':
        return JsonResponse({'lat':f"{currentCoords[0]}",
        "long":f"${currentCoords.long}"})
    if request.method == 'PUT':
        data = json.loads(request.body)
        zip = data['zip']

        coords = zipToCoord.objects.filter(zip=zip).first()
        currentCoords = [float(coords.long),float(coords.lat)]
        print(currentCoords)
        return JsonResponse({'lat':f"{currentCoords[0]}",
        "long":f"{currentCoords[1]}"})

@csrf_exempt
def getResturaunts(request):
    # Params, zip (add radius later)
    # returns resturaunts nearby as resturaunt objects
    if request.method == 'PUT':

        data = json.loads(request.body)
        zip = data['zip']
        searchRange = 20 #in miles

        coords = zipToCoord.objects.filter(zip=zip).first()
        minlong = float(coords.long) - 20/60
        maxlong = minlong + 20/60
        minlat = float(coords.lat)
        maxlat = minlat + 20/69

        #resturaunts = Resturaunt.objects.filter(long__in[minlong,maxlong])
        return JsonResponse({'resturaunts':resturaunts[0].title})


def explore(request):
    return render(request,'leaf/explore.html')



        

