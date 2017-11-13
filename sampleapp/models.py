from django.db import models

# Create your models here.
import thresher


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.ForeignKey('sampleapp.Job', null=True, blank=True)


class Job(models.Model):

    manager = models.ForeignKey(Employee, related_name='jobs_managed')
    hourly_wage = models.FloatField(default=7.25)


class Building(models.Model):

    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)


class Clock(models.Model):

    building = models.ForeignKey(Building)
    door = models.CharField(max_length=50)


class ClockIn(models.Model):

    clock = models.ForeignKey(Clock)
    employee = models.ForeignKey(Employee)
    in_at = models.DateTimeField(auto_now_add=True, editable=False)


class ClockOut(models.Model):

    clock = models.ForeignKey(Clock)
    clock_in = models.OneToOneField(ClockIn)
    out_at = models.DateTimeField(auto_now_add=True, editable=False)


class TimeRecord(models.Model):

    clock_out = models.ForeignKey(ClockOut)

    employee_first_name = thresher.FactField('employee__first_name', keep_in_sync=True)
    employee_last_name = thresher.FactField('employee__last_name', keep_in_sync=True)
    manager_first_name = thresher.FactField('manager__first_name', keep_in_sync=True)
    manager_last_name = thresher.FactField('manager__last_name', keep_in_sync=True)
    hourly_wage = thresher.FactField('employee__job__hourly_wage')
    in_at = thresher.FactField('clock_in__in_at')
    out_at = thresher.FactField('out_at')
    door_in = thresher.FactField('clock_in__clock__door')
    door_out = thresher.FactField('clock__door')
    building_name = thresher.FactField('clock__building__name')
    building_address1 = thresher.FactField('clock__building__address1')
    building_address2 = thresher.FactField('clock__building__address2')
    building_city = thresher.FactField('clock__building__city')
    building_state = thresher.FactField('clock__building__state')
    building_zipcode = thresher.FactField('clock__building__zipcode')

    # employee = thresher.RelatedFactField(source='employee')
    # manager = thresher.RelatedFactField(source='employee__job__manager')
    # building = thresher.RelatedFactField('clock__building')

    class ThresherMeta:
        base_record = 'clock_out'

    class Meta:
        managed = False  # just for now, to prevent adding to db
