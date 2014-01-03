# from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    """docstring for home_page"""
    return render(request, 'home.html')
    
def view_list(request):
    """docstring for view_list"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    """docstring for new_list"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')