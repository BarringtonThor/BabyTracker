from django.contrib import admin
from .models import Children, SleepLogs, VaccinationLogs, DiaperChangeLogs, GrowthLogs

# Register your models here.
admin.site.register(Children)
admin.site.register(SleepLogs)
admin.site.register(VaccinationLogs)
admin.site.register(DiaperChangeLogs)
admin.site.register(GrowthLogs)