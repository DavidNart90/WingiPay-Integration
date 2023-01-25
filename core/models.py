from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Payment(models.Model):
    transaction_ref = models.CharField(max_length=64, unique=True)
    amount = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')
    full_name = models.CharField(max_length=100, default='')

    def __str__(self) -> str:
        return f"Payment by {self.full_name} for {self.amount}with reference {self.transaction_ref}"


