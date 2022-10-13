from django.urls import path
from . import views

app_name='accounts' # 왜 쓸까여?
# 우리는 기본적으로 URL을 모두 변수화 해서 쓰고있음 


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/',views.update, name='update'),
    path('delete/', views.delete, name='delete')
]