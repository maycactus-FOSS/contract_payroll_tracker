from django.db import models

class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    date = models.DateField()
    place = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    travel_distance = models.DecimalField(max_digits=8, decimal_places=2)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_pdf = models.FileField(upload_to='invoices/', blank=True, null=True)

    def __str__(self):
        return f"Contract - {self.date} at {self.place}"
