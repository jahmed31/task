from django.urls import path

from .views import TaskAPI
from .authentication import CustomToken, Logout

urlpatterns = [
    path('tasks/', TaskAPI.as_view(), name='list_create'),
    path('tasks/<int:pk>/', TaskAPI.as_view(), name='detail_update_delete'),
    path('login/', CustomToken.as_view(), name='api_login'),
    path('logout/', Logout.as_view(), name='api_logout'),
]
