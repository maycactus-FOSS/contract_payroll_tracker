from django.db import models

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f"Expense - {self.description} on {self.date}"

    def delete(self, *args, **kwargs):
        if self.receipt:
            self.receipt.delete()

        super().delete(*args, **kwargs)