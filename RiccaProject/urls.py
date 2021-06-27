from django.conf.urls import url, include
from django.contrib import admin
from RICList import views 

 
urlpatterns = [    
    url('admin/',admin.site.urls),
    url(r'^$', views.HomePage, name='HomePage'),    
    url(r'^RICList/new$', views.new_list, name='new_list'),        
    url(r'^candy_list$', views.candy_list, name='candy_list'),
    url(r'^django_list$', views.django_list, name='django_list'),
    url(r'^chuchay_list$', views.chuchay_list, name='chuchay_list'),
    url(r'^kanga_list$', views.kanga_list, name='kanga_list'),
    url(r'^form_list$', views.form_list, name='form_list'),
    url(r'^RICList/form$', views.form_list, name='form_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),   
    url(r'^(\d+)/view_municipality$', views.view_municipality, name='view_municipality'),       
    url(r'^new_municipality$', views.new_municipality, name='new_municipality'),    
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^edit/(?P<id>\d+)$',views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),]