
from django.contrib import admin

from .models import customer, order, products,tag

class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','product','status','date_created')

# Register your models here.

admin.site.register(customer)
admin.site.register(products)
admin.site.register(order, OrderAdmin)
admin.site.register(tag)
