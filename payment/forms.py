from django.forms import ModelForm
from .models import PaymentDetail


class PaymentDetailsForm(ModelForm):

    class Meta:
        model = PaymentDetail
        fields = ('name','amount','email')
