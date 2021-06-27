from django.shortcuts import render, redirect
from django.http import HttpResponse
from RICList.models import Municipality, Personal, Employment, Vaccination_Details, Comorbidities


def HomePage(request):
    municipalitys= Municipality.objects.all()
    return render(request, 'model1.html', {'municipalitys': municipalitys})

def new_municipality(request):  
    newmunicipality_ = Municipality.objects.create(yybaranggay=request.POST['ffbrgy'],ukmunicipality=request.POST['xxmni'],xxregion=request.POST['Region']) 
    return redirect(f'/{newmunicipality_.id}/view_municipality')

def view_municipality(request, municipality_id):
    municipality_ = Municipality.objects.get(id=municipality_id)
    return render(request, 'model2.html', {'municipality': municipality_}) 
def add_item(request, municipality_id):    
    municipality_ = Municipality.objects.get(id=municipality_id)  
    Personal.objects.create(zflname=request.POST['fname'],znaddress=request.POST['address1'],rremail=request.POST['zemail'],zvphil=request.POST['phil1'],zpnumber=request.POST['cn'],zemerg=request.POST['Cnumber'],hhrelat=request.POST['rell'],zfccategories=request.POST['com'],rmgender=request.POST['cmm'],zbirth=request.POST['DOB'], municipality=municipality_)
    return redirect(f'/{municipality_.id}/view_municipality') 
def form_list(request):
    return render(request,'model1.html')
def candy_list(request):
    return render(request,'model2.html')
def django_list(request):
    return render(request,'model3.html')
def chuchay_list(request):
    return render(request,'model4.html')
def kanga_list(request):
    return render(request,'model5.html')
def edit(request, id):
    municipalitys = Municipality.objects.get(id=id)
    context = {'municipalitys': municipalitys}
    return render(request, 'update.html', context)
def update(request, id):
    municipality = Municipality.objects.get(id=id)
    municipality.yybaranggay =request.POST['ffbrgy']
    municipality.ukmunicipality =request.POST['xxmni']
    municipality.xxregion =request.POST['Region']
    municipality.save()
    return redirect('/')
def delete(request, id):
    municipality = Municipality.objects.get(id=id)
    municipality.delete()
    return redirect('/')
def new_list(request):
    municipality_= Municipality.objects.create()
    #municipal_= Municipality.objects.create(ukmunicipality=request.POST['flmunicipality'],yybaranggay=request.POST['zzbaranggay'])
    return redirect(f'/RICList/{municipality_.id}/')

#def add_item(request, municipality_id):
    #municipality_ = Municipality.objects.get(id=municipality_id)
    #Personal_Info.objects.create(zflname=request.POST['zvname'],znaddress=request.POST['xxaddress'],zpngender=request.POST['rjgender'],zpnumber=request.POST['contactn'],zvphilhealth=request.POST['philnumber'] ,zrmbirthday=request.POST['kkbirthday'],municipality=municipality_)
    #return redirect(f'/RICList/{municipality_.id}/')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def ikauna_list(request):
    return render(request, 'model1.html')
def two_list(request):
    return render(request, 'model2.html')
def ikatlo_list(request):
    return render(request, 'model3.html')
def ikaapat_list(request):
    return render(request, 'model4.html')
def ikalima_list(request):
    return render(request, 'model5.html')

def dataManipulation(request):
    municipality = Municipality (ukmunicipality="Dasma", yybaranggay="Paliparan III")
    municipality.save()
    
    objects = Municipality.objects.all()
    result ='Result of all entries in municipality model : <br>'
    for x in objects:
        res += x.Municipality+'<br>'
    municipalty = Municipality.objects.get(id='18')
    res += 'Only one entry <br>'
    res += hhmunicipality.Baranggay
    
    res += '<br> Delete entry <br>'
    municipality.delete()
    
    municipality = Municipality.objects(ukmunicipality = 'dasma' , yybaranggay = 'Paliparan III')
    municipality.save()
    res =""

    qs = Municipality.objects.filter(ukmunicipality = 'dasma')
    res += "Found : %s results <br>" %len(qs)

    qs = Municipality.objects.order_by('ukmunicipality')
    for x in qs:
        res += x.ukmunicipality + x.yybaranggay +'<br>'


#<table id="tablelist" name="tr">
    #{% for item in items %}
    #<tr>
        #<td>{{ item.ukmunicipality }}</td>
        #<td>{{ item.yybaranggay }}</td>
     
        
       
        
        
    #</tr>
     #{% endfor %}
#</table>
#<table id="tablelist" name='tr'>
  #{% for item in list.item_set.all %} 
      # <! -- {{ forloop.counter }}:  -->
    
    #<tr>
        #<td>{{ item.zflname }}</td>
        #<td>{{ item.znaddress }}</td>
        #<td>{{ item.zpngender }}</td>
        #<td>{{ item.zpnumber }}</td>
        #<td>{{ item.zvphilhealth }}</td>
        #<td>{{ item.zrmbirthday }}</td>
        
    #</tr>
     #{% endfor %}
#</table>


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
  

