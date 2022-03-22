from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import zipToCoord
import time
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
currentCoords = [0,0]


def populateZips():
    data = []
    file = open('C:/Users/thoma/Desktop/finalCS50W/leaftlettest/leaflet/leaf/ziptocoord.txt')
    for line in file:
        line = line.replace('\n','')
        data = line.split(',')
        obj = zipToCoord.objects.create(zip=data[0],long=data[1],lat=data[2])
        print(obj)
    



def index(request):
    return render(request,"leaf/bruh.html")

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


