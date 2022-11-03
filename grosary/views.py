from django.http import HttpResponse
from django.shortcuts import render
from main_food_data.models import Shop
from product_tital.models import Ptital

def main(request):
     mult=0
     shopdata=Shop.objects.all()
     ptital=Ptital.objects.all()
     
     
        
     sdata={'food':shopdata,'ptital':ptital}

     
         #   multi = Shop(total=mult)
          #  multi.save()
           
            #sdata={'val':val,'mult':mult}
            
      
    
   
     return render(request,"main.html",sdata)

def product_total(request):
    if request.method == 'POST':
            val=int(request.POST['val'])
            #prise=int(request.POST['pr'])
            #mult=val*prise
    return render(request,"main.html",{"qun":val})


"""
    def notes(request):
    if request.method == "POST":
        new_note = request.objects.all()
        Note.objects.add(new_note)
    return render(request, "notebook/notes.html", {
        "notes": Note.objects.all()
    })
    
    
    
    
    
    
    
    
    
    def main(request):
    mult=0
    sdata={}

  
    shopdata=Shop.objects.all()
    ptital=Ptital.objects.all()
   
    try:
        if request.method=='POST': 
            quntity=int(request.POST['quntity'])
            prise=shopdata.prise
            mult=quntity*10
            


    except:
        pass    
    sdata={'food':shopdata,'ptital':ptital,'mult':mult}
    return render(request,"main.html",sdata)
    
    def postpage(request):
    sum=0
    data={}
    try:
        if request.method == 'POST':
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            sum=n1+n2
            data={'n1':n1,'n2':n2,'output':sum}

    except:
        print("Put write values")    

    return render(request,"postpage.html",data) 
    




    
   try: 
        if request.method == 'POST':
            val=int(request.POST['val'])
            sdata={'val':val}
     except:
        pass
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   {% for x in mymembers %}
<tr>
<td><a href="update/{{ x.id }}">{{ x.id }}</a></td>
<td>{{ x.firstname }}</td>
<td>{{ x.lastname }}</td>
<td><a href="delete/{{ x.id }}">delete</a>
   
   
     path('delete/<int:id>', views.delete, name='delete'),
   
   
   def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
   
   
   
    """

    