from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('add/', views.add, name='add'),
    path('<str:registration_number>/', views.detail, name='detail'),
    path('<str:registration_number>/preview/', views.preview, name='preview'),
    path('<str:registration_number>/delete/', views.delete, name='delete'),
    path('<str:registration_number>/edit/', views.edit, name='edit'),
]
