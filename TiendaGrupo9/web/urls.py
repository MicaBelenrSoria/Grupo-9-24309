from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"),name="login"), 
    path("accounts/logout/", views.user_logout,name='logout'), 
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='web/registration/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='web/registration/password_reset.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='web/registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='web/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='web/registration/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('listado_productos', views.listado_productos, name='listado_productos'),
    path('listado_vendedores', views.VendedorListView.as_view(), name='listado_vendedores'),
    path('alta_productos', views.alta_productos, name='alta_productos'),
    path('alta_vendedor', views.alta_vendedor, name='alta_vendedor'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]

