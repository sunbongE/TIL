from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('delete/',views.delete, name='delete'),
    path('<int:pk>/',views.detail, name='detail'),
    path('<int:user_pk>/update/',views.update, name='update'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('password/', views.password, name='password'),


]
