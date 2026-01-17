from django.db import models


class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING  = "PENDING ",
        PAID = "PAID",

    class Type(models.TextChoices):
        PAYMENT  = "PAYMENT ",
        FINE = "FINE ",

    status = models.CharField(max_length=7, choices=Status.choices, default=Status.PENDING.value)
    type = models.CharField(max_length=6, choices=Type.choices, default=Type.PAYMENT.value)
    borrowing_id = models.ForeignKey(
        "borrowing.Borrowing",
        on_delete=models.CASCADE,
        related_name="payments",
    )
    session_url = models.URLField()
    session_id = models.CharField(max_length=255)
    money_to_pay = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Payment: {self.id} ({self.status})"
