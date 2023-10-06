from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
   #the comment below  was here initially  
   #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('block_user/', views.block_user, name='block_user'),
    path('unblock_user/', views.unblock_user, name='unblock_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
   # path('record/<int:pk>', views.customer_record, name='record'),
   # path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
   #path('add_record/', views.add_record, name='add_record'),
   #path('update_record/<int:pk>', views.update_record, name='update_record'),

]
