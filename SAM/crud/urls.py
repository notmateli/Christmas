from django.urls import path
from .import views


urlpatterns = [
    path("", views.crud, name="crud"),
    path("insert", views.insertData, name="insertData")

]
