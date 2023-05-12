from django.urls import path
from .import views


urlpatterns = [
    path("", views.crud, name="crud"),
    path("insert", views.insertData, name="insertData"),
    path("update/<id>", views.updateData, name="updateData"),
    path("delete/<id>", views.deleteData, name="deleteData"),
]
