from django.urls import path
from . import views
app_name='accounts'

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
