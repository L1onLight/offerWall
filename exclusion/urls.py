from django.urls import path, include
from exclusion.api import router

urlpatterns = [path("api/", include(router.urls))]
