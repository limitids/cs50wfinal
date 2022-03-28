from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('api/coords',views.zipConversion),
    path('api/resturaunts',views.getResturaunts),
    path('explore/',views.explore,name='explore'),
    path('apply/',views.resturauntApply,name='apply'),
    path('applications/',views.applicationViewer,name='applications'),
    path('api/updateApp',views.updateApp,name='updateApp')
]

