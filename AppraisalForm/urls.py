from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from AppraisalForm import views

urlpatterns = [
    path('appraisalform/', views.AppraisalForm_create, name='create_form'),
    path('appraisalform2/', views.AppraisalForm2_create, name='create_form2'),
    path('appraisalform3/', views.AppraisalForm3_create, name='create_form3'),
    
    path('appraisalform_hodcreate/', views.AppraisalForm_HODcreate,name='create_formhod'),
    path('appraisalform2_hodcreate/', views.AppraisalForm2_hodcreate, name='create_form2hod'),
    path('appraisalform3_hodcreate/', views.AppraisalForm3_hodcreate, name='create_form3hod'),
    
    path('appraisalform_hodscore/<str:user>', views.AppraisalForm_HODscores, name='staff_edit'),
    path('appraisalform_hodscore2/<str:user>', views.AppraisalForm2_HODscores, name='staff_edit2'),
    path('appraisalform_hodscore3/<str:user>', views.AppraisalForm3_HODscores, name='staff_edit3'),

    path('appraisalform_principal/<str:user>', views.AppraisalForm_Pscores, name='staff_edit_P'),
    path('appraisalform_principal2/<str:user>', views.AppraisalForm2_Pscores, name='staff_edit_P2'),
    path('appraisalform_principal3/<str:user>', views.AppraisalForm3_Pscores, name='staff_edit_P3'),

]