from django.conf.urls import url, include
from django.contrib import admin
from RICList import views 

 
urlpatterns = [    
    url('admin/',admin.site.urls),
    url(r'^$', views.HomePage, name='HomePage'),    
    url(r'^RICList/new$', views.new_list, name='new_list'),    
    url(r'^RICList/(\d+)/$', views.view_list, name='view_item'),    
    url(r'^RICList/(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^candy_list$', views.candy_list, name='candy_list'),
    url(r'^django_list$', views.django_list, name='django_list'),
    url(r'^chuchay_list$', views.chuchay_list, name='chuchay_list'),
    url(r'^kanga_list$', views.kanga_list, name='kanga_list'),
    url(r'^form_list$', views.form_list, name='form_list'),
    url(r'^RICList/form$', views.form_list, name='form_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),]
    

    


    

     # url(r'^$', 'RICSList.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
"""RiccaProject URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import url
#from RICList import views

#urlpatterns = [
    #url(r'^$', views.homepage, name='homepage'),]