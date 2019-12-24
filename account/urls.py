from django.contrib.auth import views as auth_views
from django.urls import include
from django.urls import path

from account import views as account_views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('', account_views.dashboard, name='dashboard'),
    # обратобчики входа/выхода
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # обработчики смены пароля
    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # обработчики востановления пароля
    # path('password_reset/', auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),

    path('register/', account_views.register, name='register'),
    path('edit/', account_views.edit, name='edit'),
    path('users/', account_views.user_list, name='user_list'),
    path('users/follow/', account_views.user_follow, name='user_follow'),
    path('users/<username>/', account_views.user_detail, name='user_detail'),
]
