from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts.views.userView import UserViewSet
from accounts.views.authView import RegisterView, MeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users',UserViewSet,basename='users')

urlpatterns = [
    # Auth
    path('auth/register', RegisterView.as_view(), name='auth-register'),
    path('auth/login',    TokenObtainPairView.as_view(), name='auth-login'),
    path('auth/refresh',  TokenRefreshView.as_view(),    name='auth-refresh'),
    path('auth/me',       MeView.as_view(),              name='auth-me'),
]


urlpatterns += router.urls