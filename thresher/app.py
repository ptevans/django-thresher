from django.apps import AppConfig
from django.db.models.signals import class_prepared


def model_registered(sender, **kwargs):
    from .thresher import ThresherModel
    if issubclass(sender, ThresherModel):
        sender.thresher_register_model()


class ThresherAppConfig(AppConfig):
    name = 'thresher'
    verbose_name = 'Thresher'

    def __init__(self, *args, **kwargs):
        class_prepared.connect(model_registered)
        super(ThresherAppConfig, self).__init__(*args, **kwargs)

    def ready(self):
        from .thresher import thresher_models
        for model in thresher_models:
            model.thresher_initialize()
