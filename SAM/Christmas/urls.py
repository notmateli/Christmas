from django.urls import path
from .import views

urlpatterns = [
    path("", views.chris, name="chris"),

]