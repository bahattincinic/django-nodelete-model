from django.db import models

from no_delete.models import NoDeleteModel


class Supplier(NoDeleteModel):
    name = models.CharField(max_length=255)

    default_manager = models.Manager()

    def __str__(self):
        return self.name
