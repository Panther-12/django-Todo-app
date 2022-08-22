from django.urls import path

from . import views

urlpatterns = [
path("",views.index, name="index"),
path("<int:id>", views.items, name="items"),
path("about/",views.about, name="about page"),
path("home/", views.home, name="home page"),
path("create/", views.create, name="create")

]