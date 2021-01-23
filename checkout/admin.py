from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('date', 'order_number', 'user_profile',
             'name', 'lastname',
             'email', 'phone_number', 'address',
             'county', 'city', 'postcode',
             'delivery_cost', 'order_total', 'grand_total',
             'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'name', 'lastname',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # reverse cronological order
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)