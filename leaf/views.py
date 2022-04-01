from tkinter import Menu
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import MenuItem, Resturaunt, zipToCoord,User
import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
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
        resturauntList = []
        resturaunts = Resturaunt.objects.filter(long__range=(long-0.33,long+0.33)).filter(lat__range=(lat-0.28,lat+0.28)).values()
        print(resturaunts)
        return JsonResponse({'resturaunts':list(resturaunts)})




def explore(request):
    return render(request,'leaf/explore.html',{
    })


@csrf_exempt
def resturauntApply(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        website = data['website']
        address = data['address']
        long = data['longitude']
        lat = data['latitude']

        print(long,lat)
        Resturaunt.objects.create(name=name,email=email,website=website,address=address,status='OPEN',long=long,lat=lat,creator=request.user)
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
        long = data['longitude']
        lat=data['latitude']
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

def resturauntPage(request,id):
    resturaunt = Resturaunt.objects.filter(id=id).first()
    menuitems = MenuItem.objects.filter(resturaunt=resturaunt)
    return render(request,'leaf/resturaunt.html',{
        'resturaunt':resturaunt,
        'menuitems': menuitems
    })

        
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("explore"))
        else:
            return render(request, "leaf/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "leaf/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "leaf/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "leaf/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("explore"))
    else:
        return render(request, "leaf/register.html")

@csrf_exempt
def addMenuItem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        cost = int(data['cost'])
        desc = data['desc']
        restid = data['id']
        img = data['img']
        if MenuItem.objects.filter(title=name):
            return HttpResponse(status=404)
        MenuItem.objects.create(resturaunt=Resturaunt.objects.get(id=restid),title=name,cost=cost,description=desc,img=img)
        return HttpResponse(status=200)
