from functools import partial
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from faculty import views

urlpatterns = [
    path('log-in',views.login),
    path('log-out',views.logOut),
    path('upload', views.simple_upload),
    path('faculty/', views.facultydashboard),
    path('hod/', views.hoddashboard),
    path('principal/', views.principaldashboard),
    path('adminmit/', views.admindashboard),
    path('faculty_list', views.staff_list),
    path('faculty_list_score', views.staff_list_hod_score),
    path('faculty_list_total', views.staff_list_total),
    path('faculty_list_P', views.staff_list_P),
    path('grade_filter', views.grade_dept_filter_P),
    path('backup_filter', views.backup_filter_P),
    path('grade_list_P', views.grade_list_P),
    path('grade_pdf', views.grade_pdf, name='grade_pdf'),
    path('admin_faculty', views.admin_staff_list),
    path('register', views.register),
    path('forgot_pwd/<str:user>',views.forgot_password, name='forgot_password'),
    path('reset_pwd/<str:user>',views.reset_password, name='reset_password'),
    path('change_password', views.changePassword),
    path('change_passwordD', views.changePasswordD),
    path('change_password_hod', views.changePasswordhod),
    path('change_password_princi', views.changePasswordprincipal),
    path('change_password_admin', views.changePasswordadmin),
    path('increment',views.exp_increment),
    path('backup',views.backupapiscore),
    path('delete/<str:user>',views.delete_faculty, name='deletef'),
    path('deleteforms',views.delete_allforms, name='deleteforms'),
    path('delete_backup/<str:pk>',views.delete_backup_date, name='deletebackup'),
    path('delete_exp/<str:pk>',views.delete_exp_date, name='deleteexp'),
]