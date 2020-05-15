from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('login',views.loginView, name='login'),
    path('logout',views.logout, name='logout'),
    path('auth/callback',views.Oauth, name='Oauth')
]