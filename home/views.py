from django.shortcuts import render

# Create your views here.


def time_checker():
    import datetime 
    
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    current_date = now.strftime("%Y-%m-%d")
    hour = now.hour

    if 5 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 17:
        greeting = "Good afternoon!"
    elif 17 <= hour < 21:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"

    return greeting,current_date,current_time
    


def home(request):
    
    greeting,current_date,current_time=time_checker()

    context={
        
        'title': 'CORE - Homepage',
        'hd' : 'CORE',
        'greeting': greeting,
        'current_date': current_date,
        'current_time': current_time,
    }
    return render(request,'home/index.html',context)


def dashboard(request):
    
    greeting,current_date,current_time=time_checker()

    context={
        'title': 'CORE - Dashboard',
        'hd' : 'CORE',
        'greeting': greeting,
        'current_date': current_date,
        'current_time': current_time,
    }
    return render(request,'home/dashboard.html',context)


def content(request):
    
    greeting,current_date,current_time=time_checker()

    context={
        'title': 'CORE - Content',
        'hd' : 'CORE',
        'greeting': greeting,
        'current_date': current_date,
        'current_time': current_time,
    }
    return render(request,'home/content.html',context)



def about(request):
    
    greeting,current_date,current_time=time_checker()

    context={
        'title': 'CORE - AboutUs',
        'hd' : 'CORE',
        'greeting': greeting,
        'current_date': current_date,
        'current_time': current_time,
    }
    return render(request,'home/about.html',context)
