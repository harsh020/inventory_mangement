from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from inventory.core.behaviours import StatusMixin


class Category(StatusMixin, TimeStampedModel):
    name = models.CharField(_('Name'), max_length=100, blank=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=120, db_index=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.name is not None:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class Item(StatusMixin, TimeStampedModel):
    name = models.CharField(_('Name'), max_length=200, blank=True, null=True)
    image = models.ImageField(_('Image'), blank=True, null=True, default='placeholder.png')
    description = models.TextField(_('Description'), blank=True, null=True)
    brand = models.CharField(_('Brand'), max_length=100, blank=True, null=True)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0.0)
    quantity = models.IntegerField(_('Count'), blank=True, null=True, default=0)
    category = models.ForeignKey('item.Category', on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='category_items')
    warehouse = models.ForeignKey('warehouse.Warehouse', on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name='warehouse_items')

    def __str__(self):
        return str(self.id)


