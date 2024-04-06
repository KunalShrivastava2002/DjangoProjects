from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    peoples=[
        {'name':'Kunal Shrivastava','age':21},
        {'name':'Rohit pandey','age':10},
        {'name':'Chirag gupta','age':15},
        {'name':'Nikhil arora','age':22},
        {'name':'Utkarsh yadav','age':67},
        ]
    vegetable= ['Tomato','Potato','Cabbage'] 
    # for people in peoples:
    #  print(people)

    
    return render(request, "f1/index.html",context={'page':'Django 2023 tutorial','peoples':peoples,'vegetable':vegetable}) 
def about(request):
    context= {'page':'about'}

    return render(request, "f1/about.html", context)
def contact(request):
    context= {'page':'contact'}

    return render(request, "f1/contact.html", context)

def success(request):
    return HttpResponse("<h1> MY name is kunal</h1>")

# Create your views here.
