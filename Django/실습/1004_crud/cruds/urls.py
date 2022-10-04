from django.urls import path
from . import views

app_name = 'cruds'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>',views.detail, name='detail'),
    path('<int:pk>/update/',views.update, name='update'),
    path('delete/<int:pk>',views.delete, name='delete'),
]