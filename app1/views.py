from django.shortcuts import render

# Create your views here.

# app1 related function
def home(request):
    return render(request, "app1.html")

# project related function
def home_page(request):
    return render(request, "index.html")

