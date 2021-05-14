from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('show/', views.show_data, name="showdata"),
    path('profile/<int:id>/', views.show_profile, name="showprofile"),
]
