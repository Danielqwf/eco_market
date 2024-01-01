from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, CartViewSet, InfoViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('cart', CartViewSet)
router.register('info', InfoViewSet)


urlpatterns = router.urls
