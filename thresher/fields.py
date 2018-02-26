from django.db import models

# See: https://docs.djangoproject.com/en/2.0/howto/custom-model-fields/


class FactField(object):

    def __init__(self, *args, **kwargs):
        self.source = kwargs.pop('source', None)
        self.keep_in_sync = kwargs.pop('keep_in_sync', False)
        kwargs['null'] = True
        kwargs['blank'] = True
        args, kwargs = self._custom_init(*args, **kwargs)
        super(FactField, self).__init__(*args, **kwargs)

    def _custom_init(self, *args, **kwargs):
        """Override in subclasses to provide any field specific init code"""
        return args, kwargs

    def contribute_to_class(self, cls, name, **kwargs):
        try:
            cls.thresher_register_field(self)
        except AttributeError:
            pass  #TODO: check if we are running migrations? Not OK otherwise
        return super(FactField, self).contribute_to_class(cls, name, **kwargs)

    @property
    def base_record_model(self):
        return self.model._thresher.base_record_model

    def get_source_model(self):
        source_model = self.model._thresher.base_record_model
        path_components = self.source.rsplit('__', 1)
        if len(path_components) > 1:
            model_paths = path_components[0]
            for path in model_paths.split('__'):
                field = getattr(source_model, path)
                source_model = field.field.related_model
        return source_model

    def debug(self):
        import ipdb; ipdb.set_trace()


class CharFactField(FactField, models.CharField):
    """Char"""

    def _custom_init(self, *args, **kwargs):
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 500
        return args, kwargs


class FloatFactField(FactField, models.FloatField):
    """Float"""


class IntegerFactField(FactField, models.IntegerField):
    """Int"""


class DateTimeFactField(FactField, models.DateTimeField):
    """Datetime"""

