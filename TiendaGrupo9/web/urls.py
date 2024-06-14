from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"),name="login"), 
    path("accounts/logout/", views.user_logout,name='logout'), 
    
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="web/registration/passwor_reset.html"),name="password_reset"), 
    

    path('listado_productos', views.listado_productos, name='listado_productos'),
    path('listado_vendedores', views.VendedorListView.as_view(), name='listado_vendedores'),
    path('alta_productos', views.alta_productos, name='alta_productos'),
    path('alta_vendedor', views.alta_vendedor, name='alta_vendedor'),

]

