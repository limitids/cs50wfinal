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
    file = open('C:/Users/thoma/Desktop/finalCS50W/leaftlettest/cs50wfinal/leaf/ziptocoord.txt')
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
        return JsonResponse({'long':f"{currentCoords[1]}",
        "lat":f"{currentCoords[0]}"})

@csrf_exempt
def getResturaunts(request):
    # Params, zip (add radius later)
    # returns resturaunts nearby as resturaunt objects
    if request.method == 'PUT':

        data = json.loads(request.body)
        long = float(data['long'])
        lat = float(data['lat'])
        print(long,lat)
        searchRange = 20 #in miles
        resturaunts = Resturaunt.objects.filter(long__range=(long-0.33,long+0.33)).filter(lat__range=(lat-0.28,lat+0.28))
        print(resturaunts[0].name)
        #resturaunts = Resturaunt.objects.filter(long__in[minlong,maxlong])
        return JsonResponse({'resturaunts':f"{resturaunts[0].name}"})


def explore(request):
    resturaunts = Resturaunt.objects.filter(status='OPEN')
    return render(request,'leaf/explore.html')


@csrf_exempt
def resturauntApply(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        website = data['website']
        address = data['address']

        if not Resturaunt.objects.filter(email=email):
                Resturaunt.objects.create(name=name,email=email,website=website,address=address,status='OPEN',long='0',lat='0')
                print('made')


    return render(request,'leaf/apply.html')

@csrf_exempt
def updateApp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data['status']
        name = data['name']
        address = data['address']
        email = data['email']
        website = data['website']
        long = data['long']
        lat=data['lat']
        id=data['id']
        if status == 'accepted':
            Resturaunt.objects.filter(id=id).update(status='OPEN',lat=lat,long=long,name=name,email=email,website=website,address=address)
            print(Resturaunt.objects.filter(long=long))
        else:
            Resturaunt.objects.filter(id=id).delete()
            print('deleted')
        return HttpResponse(status=200)


def applicationViewer(request):
    apps = Resturaunt.objects.filter(status='pending')
    print()
    return render(request,'leaf/applications.html',{
        'applications': apps
    })

        

