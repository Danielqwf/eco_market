from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, CartDetail

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('cart', CartDetail)

urlpatterns = router.urls
