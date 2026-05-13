from django.db import models

from books.models import Book


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book_id = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="borrowings"
    )
    user_id = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="borrowings"
    )

    def __str__(self):
        return f"Borrowing: {self.borrow_date} - {self.expected_return_date}"
