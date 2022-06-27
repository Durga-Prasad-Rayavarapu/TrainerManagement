from django.urls import path

from myapp import views

urlpatterns=[
    path('',views.home,name ='home'),
    path('logread',views.logread),#Login credentials
    #path('trainer_auth',views.trainer_auth),
    path('Register',views.trainerGet,name='reg'), #Registration Home Page
    path('trainerSet',views.trainerSet),#Registration Credentilas
    path('trainerhome', views.trainer_home, name='trainerhome'),  # trainer home page
    path('AdminHome',views.admin_home ,name='admin'),#admin Home Page
    path('trainerdetails',views.trainer_details,name='Tdetails'),#
    path('dataAssign',views.dataAssignget,),## assigning trainer for a batch
    path('dataAssignset',views.dataAssignset,name='assign'),#Batch Assigning page
    path('details',views.batch_details,name='batchd'),#batch Detailes
    path('logout',views.logout_view,name='logout'),
    path('delete/<int:id>',views.delete_batch,name='del'),
    path('update/<int:id>',views.update_batch,name='update'),
]