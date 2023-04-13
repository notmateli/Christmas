from django.urls import path
from .import views

 app_name = "tasks"
 
urlpatterns = [
    path("", views.test, name="test"),
    path("add/", views.add, name="add"),
    path("ongeza/", views.ongeza, name="ongeza"),
]

