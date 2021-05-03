from django.urls import resolve
from django.test import TestCase
from RICList.views import HomePage
from RICList.models import Item, COVIDList
from django.http import HttpRequest
from django.template.loader import render_to_string


class MyMainPage(TestCase):  
    def test_root_url_resolves_to_mainpage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage)
    def test_only_saves_items_when_necessary(self): 
        self.client.get('/')        
        self.assertEqual(Item.objects.count(), 0)
      
class COVIDListViewTest(TestCase):
 
    def test_uses_list_template(self):
        list_ = COVIDList.objects.create()        
        response = self.client.get(f'/RICList/{list_.id}/')
        self.assertTemplateUsed(response, 'submit.html')
     
   
    def test_displays_all_list_items(self):        
        list_ = COVIDList.objects.create()        
        Item.objects.create(zflname='Ricca Mae', list=list_)        
        Item.objects.create(zflname='Mique', list=list_)
   
    def test_passes_correct_list_to_template(self):       
        other_list = COVIDList.objects.create()        
        correct_list = COVIDList.objects.create()        
        response = self.client.get(f'/RICList/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)  
 
class NewCOVIDListTest(TestCase):   

    def test_redirects_after_POST(self):        
        response = self.client.post('/RICList/new', data={'flname': 'A new person','address': 'A new address','rnumber':'A new contact','rmday': 'A birthday','vaccine': 'A vaccine type'})                     
        new_list = COVIDList.objects.first()        
        self.assertRedirects(response, f'/RICList/{new_list.id}/')
       

       
class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):       
        other_list = COVIDList.objects.create()        
        correct_list = COVIDList.objects.create()        
        self.client.post(f'/RICList/{correct_list.id}/add_item', data={'flname': 'A new person','address': 'A new address','rnumber':'A new contact','rmday': 'A birthday','vaccine': 'A vaccine type'}) 
      
        self.assertEqual(Item.objects.count(), 1)        
        new_item = Item.objects.first()        
        self.assertEqual(new_item.zflname, 'A new person')       
        self.assertEqual(new_item.list, correct_list)
      
    def test_redirects_to_list_view(self):        
        other_list = COVIDList.objects.create()        
        correct_list = COVIDList.objects.create()        
        response = self.client.post(f'/RICList/{correct_list.id}/add_item',data={'flname': 'A new person','address': 'A new address','rnumber':'A new contact','rmday': 'A birthday','vaccine': 'A vaccine type'})   
        self.assertRedirects(response, f'/RICList/{correct_list.id}/')
   
class ORM(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = COVIDList()        
        list_.save()
      
        first_item = Item()        
        first_item.zflname = 'The first list item' 
        first_item.list = list_ 
        first_item.save()        
               
        second_item = Item()      
        second_item.zflname = 'Item the second'
        second_item.list = list_         
        second_item.save()
       
       
        saved_list = COVIDList.objects.first()          
        self.assertEqual(saved_list, list_)
                 
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
       
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]             
        self.assertEqual(first_saved_item.zflname, 'The first list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.zflname, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)




   

