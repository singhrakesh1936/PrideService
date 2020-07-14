from django.contrib import admin
from .models import Profile
from django.contrib import messages
from django.urls import reverse
from django.utils.html import escape, mark_safe

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	ordering = ['create_date']
	list_per_page = 50
	list_display = ( 'id', 'link_to_user','phone_number', 'state', 'city', 'gender',  'create_date', 'status')
	list_display_links = ('id','link_to_user')
	list_filter = ('status', 'gender')
	search_fields = ('phone_number', 'user__username')
	actions = ('set_assignedTo',)

	def link_to_user(self, obj):
		link = reverse("admin:auth_user_change", args=[obj.user.id])
		return mark_safe(f'<a href="{link}">{escape(obj.user.username)}</a>')

	link_to_user.short_description = 'Name'

	def set_assignedTo(self, request, queryset):
		count = queryset.update(status=True)
		self.message_user(request, 'total ' + str(count) + ' updated successfully')
		return ('services')
	set_assignedTo.short_description = 'Change Status'

