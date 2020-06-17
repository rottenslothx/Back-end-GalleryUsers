from django.contrib import admin


# Register your models here.
from review.models import Review, Gallery

admin.site.register(Review)
admin.site.register(Gallery)