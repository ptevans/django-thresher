from django.db import models

# Create your models here.
from thresher import thresher


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.ForeignKey('sampleapp.Job', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Job(models.Model):

    title = models.CharField(max_length=100)
    manager = models.ForeignKey(Employee, related_name='jobs_managed')
    hourly_wage = models.FloatField(default=7.25)

    def __str__(self):
        return self.title


class Building(models.Model):

    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Clock(models.Model):

    building = models.ForeignKey(Building)
    door = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {}'.format(self.building.name, self.door)


class ClockIn(models.Model):

    clock = models.ForeignKey(Clock)
    employee = models.ForeignKey(Employee)
    in_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} - {}'.format(self.employee, self.in_at)


class ClockOut(models.Model):

    clock = models.ForeignKey(Clock)
    clock_in = models.OneToOneField(ClockIn)
    out_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} - {}'.format(self.clock_in.employee, self.out_at)


class TimeRecord(thresher.ThresherModel):

    clock_out = models.ForeignKey(ClockOut)

    employee_first_name = thresher.CharFactField(
        source='clock_in__employee__first_name', keep_in_sync=True)
    employee_last_name = thresher.CharFactField(
        source='clock_in__employee__last_name', keep_in_sync=True)
    manager_first_name = thresher.CharFactField(
        source='clock_in__employee__job__manager__first_name', keep_in_sync=True)
    manager_last_name = thresher.CharFactField(
        source='clock_in__employee__job__manager__last_name', keep_in_sync=True)
    hourly_wage = thresher.FloatFactField(
        source='clock_in__employee__job__hourly_wage')
    in_at = thresher.DateTimeFactField(source='clock_in__in_at')
    out_at = thresher.DateTimeFactField(source='out_at')
    door_in = thresher.CharFactField(source='clock_in__clock__door')
    door_out = thresher.CharFactField(source='clock__door')
    building_name = thresher.CharFactField(source='clock__building__name')
    building_address1 = thresher.CharFactField(source='clock__building__address1')
    building_address2 = thresher.CharFactField(source='clock__building__address2')
    building_city = thresher.CharFactField(source='clock__building__city')
    building_state = thresher.CharFactField(source='clock__building__state')
    building_zipcode = thresher.CharFactField(source='clock__building__zipcode')

    class ThresherMeta:
        base_record = 'clock_out'
