from django.contrib.auth import get_user_model
from rest_framework import serializers

from books.models import Book
from borrow.models import Borrowing


User = get_user_model()


class BorrowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ("id", "book", "expected_return_date")

    def validate_book(self, book):
        if book.inventory == 0:
            raise serializers.ValidationError("Book is out of stock")
        return book

    def create(self, validated_data):
        book = validated_data.pop("book")
        book.inventory =- 1
        book.save()

        validated_data["user"] = self.context.get("request").user
        return super().create(validated_data)


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
