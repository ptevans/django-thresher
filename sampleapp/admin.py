from django.contrib import admin
from . import models

# Register your models here.

admin.site.register([
    models.Building,
    models.Clock,
    models.ClockIn,
    models.ClockOut,
    models.Employee,
    models.Job,
    models.TimeRecord,
], admin.ModelAdmin)
