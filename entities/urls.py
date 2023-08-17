from django.urls import path, include
from rest_framework import routers
from entities import views


router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'branches', views.BranchViewSet)
router.register(r'inventory', views.InventoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]