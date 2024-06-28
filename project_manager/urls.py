from django.urls import path, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (UserViewSet, get_user_details, update_user, delete_user, register_user, LoginView, ProjectViewSet,
                    TaskViewSet, task_in_project, comments_in_task, comment_detail)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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