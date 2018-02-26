from django.db import models
from django.db.models.signals import post_save

from .fields import (CharFactField, FloatFactField, IntegerFactField,
                     DateTimeFactField)


thresher_models = set()


class ThresherOptions(object):

    def __init__(self, model):
        self.base_record = None
        self.base_record_model = None
        self.fields = {}
        self.model = model

    def set_base_record(self, base_record):
        self.base_record = base_record
        field = getattr(self.model, base_record)
        self.base_record_model = field.field.related_model


def base_record_receiver(cls):
    def func(sender, instance, created, raw, using, update_fields):
        if created:
            cls.thresher_new_record(sender, instance, created, raw, using, update_fields)
    return func


class ThresherModel(models.Model):

    _thresher = None

    class Meta:
        abstract = True

    @classmethod
    def thresher_init_meta(cls):
        cls._thresher = ThresherOptions(cls)

    @classmethod
    def thresher_register_field(cls, field):
        if cls._thresher is None:
            cls.thresher_init_meta()
        cls._thresher.fields[field.source] = field

    @classmethod
    def thresher_register_model(cls):
        thresher_models.add(cls)

    @classmethod
    def thresher_initialize(cls):
        cls._thresher.set_base_record(cls.ThresherMeta.base_record)
        cls.thresher_register_signals()

    @classmethod
    def thresher_register_signals(cls):
        post_save.connect(cls.thresher_new_record,
                          sender=cls._thresher.base_record_model)
        for field_path, field in cls._thresher.fields.items():
            pass
            # TODO: register signals to watch for updates
            #print(field_path, field.attname, field.name, field.get_source_model())
            #field.debug()

    @classmethod
    def thresher_new_record(cls, sender, instance, created, raw, using,
                            update_fields, **kwargs):
        model = cls._thresher.base_record_model
        values = model.objects.filter(
            pk=instance.id).values(*cls._thresher.fields.keys())[0]
        data = {cls._thresher.fields[k].attname: v for k, v in values.items()}
        data[cls._thresher.base_record] = instance
        print(data)
        cls.objects.create(**data)



