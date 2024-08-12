from django.contrib import admin
from .models import *


class CourierAdmin(admin.ModelAdmin):
	list_display = ('tracking_id','sender_name', 'status',)
	list_display_links = ('tracking_id','sender_name',)
	# change_list_template = 'admin/change_list.html'
	actions = None
	list_per_page = 25

class ShippingHistroyAdmin(admin.ModelAdmin):
	list_display = ( 'parcel', 'date')
	list_per_page = 20
	

admin.site.site_header = 'Skyxpress-Delivery-Logistics-ADMIN'
admin.site.site_title = 'Skyxpress-Delivery-Logistics-ADMINISTRATION'
admin.site.register(Courier, CourierAdmin)
admin.site.register(ShippingHistroy, ShippingHistroyAdmin)
admin.site.register(Contact)
admin.site.register(Quote)

