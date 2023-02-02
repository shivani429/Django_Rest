"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from firstapp import views 


urlpatterns = [
    path('', include('firstapp.urls')),
    path('admin/',admin.site.urls),
    path('add',views.studentlistcreate.as_view()),
    path('dis/<int:pk>/',views.studentdisplay.as_view()),
    path('api',views.studentlist.as_view()),
    path('create', views.studentcreate.as_view()),
    path('up/<int:pk>',views.studentup.as_view()),
    path('display/<int:pk>',views.studentrev.as_view()),
    path('del/<int:pk>',views.studentdel.as_view()),
    path('lc/',views.studentlistcreate.as_view()),
    path('ru/<int:pk>',views.studentrevup.as_view()),
    path('rdel/<int:pk>',views.studentrevdel.as_view()),
    path('rudel/<int:pk>',views.studentrevupdel.as_view()),
    
]
