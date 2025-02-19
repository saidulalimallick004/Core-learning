from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def recipes(request):
    
    if request.method=="POST":
        try:
            data=request.POST
            image=request.FILES.get('R_Image')
            r_name=data.get('Name')
            r_dec=data.get('Description')
            
            recipe.objects.create(Name=r_name,Descriptions=r_dec, R_Image=image)
            
            
            
            Message= f" A new recipe is created Successfully!!\nName: {r_name}"
        except:
            
            Message="Something went wrong!!!"
            
            
        all_Recipe=recipe.objects.all()
        
        context={
            'message':Message,
            'all_Recipe': all_Recipe
        }
        return render(request,'view_recipe.html',context)
    
    return render(request, 'new_recipe.html')



def view_recipes(request):
    
    all_Recipe=recipe.objects.all()
    
    context={
        'all_Recipe': all_Recipe
        
    }
    
    return render(request,'view_recipe.html',context)
    


def delete_recipe(request,id):
    
    
    
    recipe.objects.filter(id=id).delete()
    all_Recipe=recipe.objects.all()
    
    context={
        'all_Recipe': all_Recipe
        
    }
    
    
    return render(request,'view_recipe.html',context)


def edit_recipe(request,id):
    if request.method=="POST":
        
        try:
            data=request.POST
        
            name=data.get('Name')
            dec=data.get('Descriptions')
            
            recipe.objects.filter(id=id).update(Name=name, Descriptions=dec )
            
            message='Your Edit Request Processed Successful.\nUpdated!!'
            
        except:
            message='Sorry! Facing Some problem\nTry Again!!' 
        
        
        
        
        all_Recipe=recipe.objects.all()
        
        context={
            'message':message,
            'all_Recipe': all_Recipe
            }    
        return render(request,'view_recipe.html',context)
        
    
    quary=recipe.objects.get(id=id)
    
    
    context={
        'recipe': quary
    }
    
    
    
    return render(request, 'edit_recipe.html',context)