from django.urls import path
from .import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("Emobilis", views.emobilis),
    path("home", views.home),




]
