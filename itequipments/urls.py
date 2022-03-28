
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    # Home and Auth
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),

    # Application
    path('all_equipment/', views.all_equipment, name='all_equipment'),
    path('all_equipment_search/', views.all_equipment_search, name='all_equipment_search'),
    path('not_used_equipment/', views.not_used_equipment, name='not_used_equipment'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('view_equipment/<int:log_pk>', views.view_equipment, name='view_equipment'),
    path('view_not_equipment/<int:log_pk>', views.view_not_equipment, name='view_not_equipment'),
    path('edit_equipment/<int:log_pk>', views.edit_equipment, name='edit_equipment'),
    path('edit_not_equipment/<int:log_pk>', views.edit_not_equipment, name='edit_not_equipment'),
    path('edit_equipment/<int:log_pk>/delete', views.delete_equipment, name='delete_equipment'),
]
