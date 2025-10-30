from rest_framework.routers import DefaultRouter
from accounts.views.userView import UserViewSet

router = DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = router.urls

