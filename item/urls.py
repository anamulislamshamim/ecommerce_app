from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]