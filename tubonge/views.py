from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def nav(request):
    return render(request , 'navbar.html')
def about(request):
    return render(request,'about.html')
def footer(request):
    return render(request,'footer.html')
def contact(request):
    return render(request,'contact.html')