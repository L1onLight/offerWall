from rest_framework.routers import DefaultRouter

from exclusion.views import ExclusionViewSet

router = DefaultRouter()

router.register(r'exclusion', ExclusionViewSet, basename='exclusion')
