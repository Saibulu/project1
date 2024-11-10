from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def starterpage(request):
    return render(request,'starter-page.html')

def servicepage(request):
    return render(request,'service-details.html')