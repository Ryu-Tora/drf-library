from django.contrib.auth import get_user_model
from rest_framework import serializers

from books.models import Book
from borrow.models import Borrowing


User = get_user_model()


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ("id", "borrow_date", "expected_return_date", "actual_return_date", "book_id", "user_id")
        readonly_fields = ("id", "borrow_date", "expected_return_date")


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
        read_only_fields = ("id", "username", "email", "first_name", "last_name")


class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "cover", "inventory", "daily_fee")
        read_only_fields = ("id", "title", "author", "cover", "inventory", "daily_fee")


class BorrowingDetailSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()
    book = BookShortSerializer()

    class Meta:
        model = Borrowing
        fields = ("id", "borrow_date", "expected_return_date", "actual_return_date", "book", "user")
        read_only_fields = ("id", "borrow_date", "expected_return_date", "book", "user")
