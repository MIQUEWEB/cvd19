from django.shortcuts import render, redirect
from django.http import HttpResponse
from RICList.models import Item, COVIDList


def HomePage(request):
    items = Item.objects.all()
    return render(request, 'homepage.html',{'items' : items})
    


def view_list(request, list_id):
    list_ = COVIDList.objects.get(id=list_id)
    return render(request, 'submit.html', {'list': list_})


def new_list(request):
    list_ = COVIDList.objects.create()
    Item.objects.create(zflname=request.POST['flname'],znaddress =request.POST['address'],zpnumber=request.POST['rnumber'],zrmbirthday =request.POST['rmday'],zvaccine =request.POST['vaccine'], list=list_)
    return redirect(f'/RICList/{list_.id}/')

def add_item(request, list_id):
    list_ = COVIDList.objects.get(id=list_id)
    Item.objects.create(zflname=request.POST['flname'],znaddress =request.POST['address'],zpnumber=request.POST['rnumber'],zrmbirthday =request.POST['rmday'],zvaccine =request.POST['vaccine'], list=list_)
    return redirect(f'/RICList/{list_.id}/')







#def homepage(request):
    #if request.method == 'POST':
        #Item.objects.create(text=request.POST['    peronEntry'])
        #return redirect('/')
    #items = Item.objects.all()
    #return render(request, 'homepage.html', {'newPerson': items})





#From RICCOVIDList.models import Item

#def homepage(request):
 #return render(request,'homepage.html',
    #items = Item.objects.all()
    #print(request.POST)
    #return render(request,"homepage.html",{'fname':requesst.POST.get('fname',''),'aaddress':request.POST.get('address','')


 #{'new_entry_text':request.POST.get('name',''),})
  
  # return HttpResponse('homepage')
 #return render(request,'homepage.html')
 
 
 
 #test # new test in test.py, and the view in views.py
 #basic view
 #from django.shortcuts import render
 #from django.http import HttpResponse
 
 #def home_page(request):
 # return HttpResponse('<html><title>Kdrama Suggest><title></html>')
 #create your views here.
  # return HttpResponse('homepage')
  
