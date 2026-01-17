from django.urls import path, include
from rest_framework import routers

from borrow.views import BorrowingViewSet

router = routers.DefaultRouter()
router.register("borrowing", BorrowingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
