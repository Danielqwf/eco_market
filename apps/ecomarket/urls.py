from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, Cart

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('cart', Cart)

urlpatterns = router.urls
