from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNew

# Create your views here.
# python3 manage.py runserver
# pythone manage.py shell
# python3 manage.py startapp <name>
# python3 manage.py createsuperuser
# django-admin startproject <name> 

def index(response):

	items = ToDoList.objects.all()
	return render(response, "main/landing.html")

def about(response):
	return HttpResponse('<h2> about page</h2')


# Home page url handler
def home(response):
	items = ToDoList.objects.all()

	return render(response, "main/homepage.html",{"items":items}) 

def items(response, id):
	lists = ToDoList.objects.get(id=id)

	if response.method == "POST":
		# data from input field with name "save"
		if response.POST.get("save"):
			for item in lists.item_set.all():
				if response.POST.get("c"+str(item.id)) == "checked":
					item.complete= True
				else:
					item.complete = False
				item.save()
		elif response.POST.get("newItem"):
			text = response.POST.get("new")

			if len(text) >2:
				lists.item_set.create(text=text, complete=False)
 
	#context = {
	#	'lists':lists,
	#}
	return render(response, "main/items.html", {"lists":lists})

# create a new todo list
# Getting info from a form
def create(response):
	if response.method =="POST":
		# Passes the values in the form
		form = CreateNew(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			# Redirect to another route or url
		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNew()

	return render(response, "main/create.html", {"form":form} )	