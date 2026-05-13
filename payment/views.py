from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from payment.models import Payment
from payment.permissions import IsOwnerOrAdmin
from payment.serializers import PaymentDetailSerializer, PaymentSerializer


class PaymentViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = Payment.objects.all()

    def get_queryset(self):
        queryset = Payment.objects.select_related(
            "borrowing", "borrowing__user"
        )
        if self.request.user.is_staff:
            return queryset

        return queryset.filter(borrowing__user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PaymentDetailSerializer
        return PaymentSerializer
