from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, get_user_details, update_user, delete_user, register_user, LoginView, ProjectViewSet,
                    TaskViewSet, task_in_project, comments_in_task, comment_detail)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('users/register/', register_user, name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/<int:id>/', get_user_details, name='user-details'),
    path('users/<int:id>/update/', update_user, name='user-update'),
    path('users/<int:id>/delete/', delete_user, name='user-delete'),
    path('projects/<int:project_id>/tasks/', task_in_project, name='project-tasks'),
    path('tasks/<int:task_id>/comments/', comments_in_task, name='comments-in-task'),
    path('comments/<int:id>/', comment_detail, name='comment-detail'),
]

urlpatterns += router.urls