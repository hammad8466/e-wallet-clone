from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up,name='signup'),
    path('login/', views.user_login,name='login'),
    path('profile/', views.user_profile,name='profile'),
    path('logout/', views.user_logout,name='logout'),
    path('changepass/', views.user_change_pass,name='changepass'),
    path('home/', views.home, name='home'), 
    path('transfer/', views.transfer_funds, name='transfer_funds'),
    path('account-statement/', views.account_statement, name='account_statement'),
    path('add-friend/', views.add_friend, name='add_friend'),
    path('friends-list/', views.friends_list, name='friends_list'), 
    path('statement-history/', views.admin_statement_history, name='admin_statement_history'),
    path('load-balance/', views.admin_load_balance, name='admin_load_balance'),
    path('change_email/', views.user_change_email, name='change_email'),
    path('admin_dashboard/', views.admin_dashboard,name='admin_dashboard'),
]
