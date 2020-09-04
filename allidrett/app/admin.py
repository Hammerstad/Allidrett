from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('email','name','get_party_id','year_of_birth')

    def get_party_id(self, obj):
        return "%s %s-%s" % (obj.party.day, obj.party.start_time, obj.party.end_time)
    get_party_id.short_description = 'party'
    get_party_id.admin_order_field = 'party__id'