"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import *
from recepie.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    #--------------------------------------------------

    path('',home,name='home'),
    path('home/',home,name='home'),
    path('dashboard/',dashboard,name='dashboard'),
    path('content/',content,name='content'),
    path('about/',about,name='about'),
    
    #---------------------------------------------------
    
    path('recipe/',recipes,name="recipe"),
    path('view_recipe/',view_recipes,name="view_recipe"),
    path('edit_recipe/<id>',edit_recipe,name="edit_recipe"),
    path('delete_recipe/<id>',delete_recipe,name="delete_recipe"),
    
    
    path('login_page/',login_page,name='login_page'),
    path('registration_page/',registration_page,name='register_page')
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    
urlpatterns += staticfiles_urlpatterns()
