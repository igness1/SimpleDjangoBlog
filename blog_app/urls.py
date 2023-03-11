from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout')
]
