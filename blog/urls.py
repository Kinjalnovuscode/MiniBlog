from django.contrib import admin
from django.urls import path ,include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path ('addpost/', views.add_post, name='addpost'),
    path ('updatepost/<int:id>', views.update_post, name='updatepost'),
    path ('deletepost/<int:id>',views.delete_post,name='deletepost'),
]
