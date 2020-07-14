from django.contrib import admin
from .models import Services
from .models import States
from .models import Cities

admin.site.register(Services)
admin.site.register(Cities)
admin.site.register(States)