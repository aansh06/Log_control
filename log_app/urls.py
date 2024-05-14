from django.urls import path
from . import views

urlpatterns =[
    path('', views.home , name='home'),
    path('fetch_user_data/', views.fetch_user_data, name='fetch_user_data'),
    path('process_transaction/', views.process_transaction, name='process_transaction'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('create_data/', views.create_data, name='create_data'),
    path('read_data/', views.read_data, name='read_data'),
    path('update_data/', views.update_data, name='update_data'),
    path('delete_data/', views.delete_data, name='delete_data'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('download_file/', views.download_file, name='download_file'),
    path('search_data/', views.search_data, name='search_data'),
    path('send_email/', views.send_email, name='send_email'),
    path('send_notification/', views.send_notification, name='send_notification'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('external_service_integration/', views.external_service_integration, name='external_service_integration'),
]