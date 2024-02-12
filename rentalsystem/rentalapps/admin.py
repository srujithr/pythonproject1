from django.contrib import admin
from.models import customusers,Car,Booking
from django.contrib.auth.models import Group
# Register your models here.


class CustomusersAdmin(admin.ModelAdmin):
    list_display = ('username','email','address','phone')
    search_fields = ('first_name','last_name','email')
    list_filter = ()
    list_per_page = 10
    readonly_fields = ('first_name','last_name','username','email','address','company_name','phone')


class CarAdmin(admin.ModelAdmin):
    list_display = ('company_id','name','image','car_model','price','details')
    search_fields = ('company_id',)
    list_per_page = 10
    readonly_fields = ('company_id','name','image','car_model','price','details')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','car','no_of_days','day','Total_cost','booking_date','status','review','Rating')
    search_fields = ('user','car','no_of_days')
    list_filter = ('user','car')
    list_per_page = 10
    readonly_fields =('user','car','no_of_days','day','Total_cost','booking_date','status','review','Rating')


admin.site.register(customusers,CustomusersAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Car,CarAdmin)

admin.site.unregister(Group)

admin.site.site_header = 'Car Rental System'


