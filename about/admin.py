from django.contrib import admin
from .models import School
from .models import Interest
from .models import Company
from .models import Social

# Register your models here.

admin.site.register(School)
admin.site.register(Interest)
admin.site.register(Company)
admin.site.register(Social)