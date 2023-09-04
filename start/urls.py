from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.introduction, name='introduction'),
    path('register/', views.registerform, name='register'),
    path('login/', views.loginform, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name= 'profile'),
    path('upchange/', views.userpasswordchange, name= 'upchange'),
    path('contact/', views.contact, name= 'contact'),
    path('userupdate/', views.userupdate, name= 'userupdate'),
    path('myworks/', views.myworks, name= 'myworks'),
    path('likedblogs/', views.likedblogs, name= 'likedblogs'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),

    path('subscriptions/', views.subscriptions, name= 'subscriptions'),
    # path('bloggers/', views.bloggers, name= 'bloggers'),

    path('searchbar/', views.searchbar, name = 'searchbar')
    # path('searchbar/', views.search_blog, name = 'searchbar')
]