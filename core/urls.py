from rest_framework.routers import SimpleRouter

from core.views import LessonViewSet, ProductViewSet

router = SimpleRouter()

router.register('lessons', LessonViewSet, basename='lessons')
router.register('products', ProductViewSet, basename='products')
