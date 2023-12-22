from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, Cart, ProductSearchView

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('cart', Cart)

urlpatterns = [
    path('product-search/', ProductSearchView.as_view())
]



urlpatterns += router.urls
