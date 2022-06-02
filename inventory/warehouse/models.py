from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from inventory.core.behaviours import StatusMixin


class Warehouse(StatusMixin, TimeStampedModel):
    name = models.CharField(_('Name'), max_length=100, blank=True, null=True)
    address = models.OneToOneField('core.Address', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)
