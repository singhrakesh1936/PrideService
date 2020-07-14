from __future__ import unicode_literals
from django.contrib import admin
from .models import PaymentDetail,RazorpayResponsew

@admin.register(PaymentDetail)
class ProfileAdmin(admin.ModelAdmin):
	list_per_page = 50
	list_display = ( 'id', 'uuid','name', 'PayType', 'amount', 'email','active','created_on')
	list_display_links = ('id',)
	list_filter = ( 'created_on','PayType','email')
	search_fields = ('uuid', 'PayType','name','created_on')

@admin.register(RazorpayResponsew)
class RazorpayResponseAdmin(admin.ModelAdmin):
	list_per_page = 50
	list_display = ( 'id', 'uuid',  'relation', 'active','created_on',)
	list_display_links = ('id',)
	list_filter = ( 'created_on','active')
	search_fields = ('uuid', 'created_on','relation__email')