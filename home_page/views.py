from django.shortcuts import render

def home(request):
    return render(request,'home/home.html')


def aboutus(request):
    return render(request,'about/about.html')
