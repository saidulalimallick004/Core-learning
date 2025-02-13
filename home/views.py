from django.shortcuts import render

# Create your views here.



def home(request):
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
    
    context={
        'title': 'CORE',
        'greeting': greeting,
        'current_date': current_date,
        'current_time': current_time,
    }
    return render(request,'home/index.html',context)