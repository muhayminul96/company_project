from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, get_user_details, update_user, delete_user, register_user, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('api/users/register/', register_user, name='user-register'),
    path('api/users/login/', LoginView.as_view(), name='user-login'),
    path('api/users/<int:id>/', get_user_details, name='user-details'),
    path('api/users/<int:id>/update/', update_user, name='user-update'),
    path('api/users/<int:id>/delete/', delete_user, name='user-delete'),
]

urlpatterns += router.urls