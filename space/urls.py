from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # home_view endi views.py da bor
    path('dashboard/', views.s_dashboard, name='student_dashboard'),
    path('create-assignment/', views.create_post, name='create_post'),
    path('solve/<int:pk>/', views.solve_assignment, name='solve_assignment'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]