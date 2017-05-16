from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible

from no_delete.models import NoDeleteModel


@python_2_unicode_compatible
class Supplier(NoDeleteModel):
    name = models.CharField(max_length=255)

    default_manager = models.Manager()

    def __str__(self):
        return smart_text(self.name)
