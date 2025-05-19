from . import views
from django.urls import path


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('create/create/', views.task_create, name='task_create'),
    path('update/<int:pk>/edit/', views.task_update, name='task_update'),
    path('delete/<int:pk>/delete/', views.task_delete, name='task_delete')
]
