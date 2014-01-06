# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from lists.models import Item, List

def home_page(request):
    """docstring for home_page"""
    return render(request, 'home.html')
    
def view_list(request, list_id):
    """docstring for view_list"""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    """docstring for new_list"""
    list_ = List.objects.create()
    try:
        Item.objects.create(text=request.POST['item_text'], list=list_)
    except ValidationError:
        error_text = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error_text})
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
    """docstring for add_item"""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))