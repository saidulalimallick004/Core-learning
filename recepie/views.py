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
            
            
            
            print(f" A new recipe is created Successfully!!\nName: {r_name} \nDescription: {r_dec}\nImage: {image}")
        except:
            
            print("Something went wrong!!!")
            
        return redirect('/recipe/')
    
    return render(request, 'new_recipe.html')



def view_recipes(request):
    
    all_Recipe=recipe.objects.all()
    
    context={
        'all_Recipe': all_Recipe
        
    }
    
    return render(request,'view_recipe.html',context)
    