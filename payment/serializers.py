from rest_framework import serializers

from borrow.models import Borrowing
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id", "status", "type", "money_to_pay")


class BorrowingShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ("id", "borrow_date", "expected_return_date", "actual_return_date")


class PaymentDetailSerializer(serializers.ModelSerializer):
    borrowing = BorrowingShortSerializer()

    class Meta:
        model = Payment
        fields = (
            "id",
            "status",
            "type",
            "money_to_pay",
            "session_url",
            "session_id",
            "borrowing",
        )
