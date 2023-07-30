from django.db import models

class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    date = models.DateField()
    place = models.CharField(max_length=25)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    travel_distance = models.DecimalField(max_digits=8, decimal_places=2)
    invoice = models.FileField(upload_to='invoices/', blank=True, null=True)

    def __str__(self):
        return f"Contract - {self.date} at {self.place}"

    def delete(self, *args, **kwargs):
        if self.invoice:
            self.invoice.delete()

        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Check if the contract is being updated and the invoice field is being cleared
        if self.pk:
            old_contract = Contract.objects.get(pk=self.pk)
            if old_contract.invoice and not self.invoice:
                # If the invoice field is being cleared, delete the old file from the media directory
                old_contract.invoice.delete(save=False)  # Use save=False to avoid deleting the model instance from the database

        super().save(*args, **kwargs)