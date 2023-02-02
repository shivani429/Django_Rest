from argparse import Namespace
from django.urls import path,include
from .views import *
from firstapp import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('data', views.studentviewset,basename='student')
urlpatterns = [
    path('home',home),
    path('demo',demo),
    path('add/',post_student),
    path('update/<int:id>/', update_student),
    path('delete/<int:id>/', delete_student),
    # path('',include(router.urls)),

   
]