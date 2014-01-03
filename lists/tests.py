from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        """docstring for test_saving_and_retrieving_items"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        """docstring for test_root_url_resolves_to_home_page_view"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        """docstring for test_home_page_returns_correct_html"""
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        
    def test_home_page_can_save_a_POST_request(self):
        """docstring for test_home_page_can_save_a_POST_request"""
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_redirects_after_POST(self):
        """docstring for test_home_page_redirects_after_POST"""
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
                
    def test_home_page_only_saves_items_when_necessary(self):
        """docstring for test_home_page_only_saves_items_when_necessary"""
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.all().count(), 0)
                
class ListViewTest(TestCase):
    """docstring for ListViewTest"""

    def test_ises_list_templates(self):
        """docstring for test_ises_list_templates"""
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')
        
    def test_displays_all_items(self):
        """docstring for test_displays_all_items"""
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        response = self.client.get('/lists/the-only-list-in-the-world/')
        
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')