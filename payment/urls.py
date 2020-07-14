from django.conf.urls import url
from .views import StoreDetails, MyPayment, home


urlpatterns = [
	url('org', StoreDetails.as_view(), name='org'),
    url('payment', MyPayment.as_view(), name='payment'),
    url('', home, name='home'),
	]
