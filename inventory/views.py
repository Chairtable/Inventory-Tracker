from django.shortcuts import render, redirect  
from inventory.forms import InventoryForm  
from inventory.models import Inventory
from django.http import HttpResponse
import csv  

def index(request):  
    inventoryFull = Inventory.objects.all()  
    return render(request,"index.html",{'inventoryFull':inventoryFull})      

def add(request):  
    if request.method == "POST":  
        form = InventoryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass  
    else:  
        form = InventoryForm()  
    return render(request,'add.html',{'form':form})

def edit(request, id):  
    inventory = Inventory.objects.get(id = id)  
    return render(request,'edit.html', {'inventory':inventory})  

def update(request, id):  
    inventory = Inventory.objects.get(id=id)  
    form = InventoryForm(request.POST, instance = inventory)  
    if form.is_valid():  
        form.save()  
        return redirect("/index")  
    return render(request, 'edit.html', {'inventory':inventory})  

def remove(request, id):  
    inventory = Inventory.objects.get(id = id)  
    inventory.delete()  
    return redirect("/index")

def exportcsv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition':'attachment; filename="Product_Data.csv"'},
    )
    inventoryFull = Inventory.objects.all()  
    writer = csv.writer(response)  
    for item in inventoryFull:  
        writer.writerow([item.iid,item.iname,item.iquantity])  
    return response 

