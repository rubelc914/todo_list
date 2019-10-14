from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method=='POST':
        form=ListForm(request.POST or None)

        if form. is_valid():
            form.save()
            all_items=List.objects.all
            messages.info(request,('Item has been added to list!'))
            return render(request,'home.html',{'all_items':all_items})
    else:
         all_items=List.objects.all
         return render(request,'home.html',{'all_items':all_items})



def delete(request,id):
    item=List.objects.get(pk=id)
    item.delete()
    messages.success(request,'item has been deleted ')
    return redirect('home')


def cross_off(request,id):
    item=List.objects.get(pk=id)
    item.complete= True
    item.save()
    return redirect('home')

def uncross(request,id):
    item= List.objects.get(pk=id)
    item.complete= False
    item.save()
    return redirect('home')

def edit(request,id):
    if request.method=='POST':
        item=List.objects.get(pk=id)

        form=ListForm(request.POST or None,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'list Edit has been successfull!!')
            return redirect('home')
    else:
        item=List.objects.get(pk=id)
        return render(request,'edit.html',{'item':item})
