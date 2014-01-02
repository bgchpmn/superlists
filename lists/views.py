from django.shortcuts import render

# Create your views here.
def home_page(request):
    """docstring for home_page"""
    return render(request, 'home.html')