from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('api/coords',views.zipConversion),
    path('api/resturaunts',views.getResturaunts),
    path('explore/',views.explore,name='explore'),
    path('apply/',views.resturauntApply,name='apply'),
    path('applications/',views.applicationViewer,name='applications'),
    path('api/updateApp',views.updateApp,name='updateApp'),
    path('resturaunt/<int:id>',views.resturauntPage),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('api/menuItem',views.addMenuItem,name='updateApp'),


]

