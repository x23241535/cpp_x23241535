from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.mainpage, name='main_website'),  # Set main_website as the root URL
    path('admin_login/', views.admin_login, name='admin_login'),
    path('staff/', views.index, name='index'),
    path('user_firstpage/', views.user_firstpage, name='user_firstpage'),
    path('update_appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('bmiUI/', views.bmiUI, name='bmiUI'),
    # Add more URL patterns as needed
]
urlpatterns += staticfiles_urlpatterns()
