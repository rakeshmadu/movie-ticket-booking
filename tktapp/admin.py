from django.contrib import admin
from .models import Movies,Theatre,Signup,Booking
# Register your models here.
admin.site.register(Movies)
admin.site.register(Theatre)
admin.site.register(Signup)
admin.site.register(Booking)
