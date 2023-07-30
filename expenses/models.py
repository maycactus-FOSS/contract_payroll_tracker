from django.db import models

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    date = models.DateField()
    description = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f"Expense - {self.description} on {self.date}"

    def delete(self, *args, **kwargs):
        if self.receipt:
            self.receipt.delete()

        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Check if the expense is being updated and the receipt field is being cleared
        if self.pk:
            old_expense = Expense.objects.get(pk=self.pk)
            if old_expense.receipt and not self.receipt:
                # If the receipt field is being cleared, delete the old file from the media directory
                old_expense.receipt.delete(save=False)  # Use save=False to avoid deleting the model instance from the database

        super().save(*args, **kwargs)