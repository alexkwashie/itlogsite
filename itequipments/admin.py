from django.contrib import admin
from . models import All_equipment

# Register your models here.
class All_equipmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)


admin.site.register(All_equipment,All_equipmentAdmin)