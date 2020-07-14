import requests
from django.conf import settings
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import PaymentDetailsForm
from .models import PaymentDetail,RazorpayResponsew

key = settings.RAZOR_KEY_ID
secret = settings.RAZOR_KEY_SECRET


def home(request):

    return render(request, 'home.html')


class StoreDetails(View):

    def get(self, request):
        template = 'store_user_details.html'
        form = PaymentDetailsForm()
        return render(request, template, locals())

    def post(self, request):
        form = PaymentDetailsForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            template = 'get_user_details.html'
        else:
            form = PaymentDetailsForm()
            template = 'store_user_details.html'
        return render(request, template, locals())


@method_decorator(csrf_exempt, name='dispatch')
class MyPayment(View):

    def post(self, request):

        template = 'success.html'
        # import ipdb;ipdb.set_trace()
        try:

            print(request.POST)
            reps = request.POST.dict()

            payment_id =reps['razorpay_payment_id']

            reference_obj = reps['payment_order_id'].replace('-', '')
            print(reference_obj)
            reference_obj_amount = reps['payment_order_amount']

            real_obj = PaymentDetail.objects.get(uuid=reference_obj)
            print("-1")
            if int(real_obj.amount) == int(reference_obj_amount):
                url = 'https://api.razorpay.com/v1/payments/%s/capture' % str(payment_id)
                resp = requests.post(url, data={'amount': int(real_obj.amount) * 100}, auth=(key, secret))
                print("a")
                if resp.status_code == 200:
                    data = {"body": request.body, "contetn": resp.text}
                    RazorpayResponsew.objects.create(response=data, status=2, relation_id=int(real_obj.id))
                    response = "Success"
                    print("b")
                elif resp.status_code == 400:
                    data = {"body": request.body, "contetn": resp.text}
                    RazorpayResponsew.objects.create(response=data, status=0, relation_id=int(real_obj.id))
                    response = "Failed we will verify shortly"
                    print("c")
                    # send_mail()
                else:
                    data = {"body": request.body, "contetn": resp.text}
                    RazorpayResponsew.objects.create(response=data, status=1, relation_id=int(real_obj.id))
                    response = "Failed we will verify shortly"
                    print("d")
            else:
                response = "This activity logged"
        except Exception as e:
            # send_mail(e.message + pg views)
            response = "OOPS.......... Failed"
        return render(request, template, locals())
