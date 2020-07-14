from django.db import models
import uuid

PAYMENT_TYPE = ((2, "Full_Payment"), (1, "Partial_Sattlement"), (0, "Advance_Pay"))

PAYMENT_STATUS = ((2, "Success"), (1, 'Pending'), (0, 'Failed'))

class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class PaymentDetail(Base):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    PayType = models.IntegerField(choices=PAYMENT_TYPE, default="2")
    amount = models.PositiveIntegerField()
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.email

class RazorpayResponsew(Base):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    response = models.TextField()
    status = models.CharField(max_length=2, choices=PAYMENT_STATUS)
    relation = models.ForeignKey(PaymentDetail, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.relation.email + " " + str(self.id)
