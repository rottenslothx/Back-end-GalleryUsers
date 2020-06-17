from django.contrib import admin

# Register your models here.
from account.models import Users

admin.site.register(Users)