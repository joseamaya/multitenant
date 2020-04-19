from rest_framework import routers

from store.views import CategoryViewSet

router = routers.SimpleRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'products', CategoryViewSet)

urlpatterns = router.urls