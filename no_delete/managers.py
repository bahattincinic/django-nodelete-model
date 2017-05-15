from django.db import models

from .queryset import NoDeleteQueryset


class NoDeleteManager(models.Manager):

    def get_queryset(self):
        queryset = NoDeleteQueryset(self.model, using=self._db)
        return queryset.filter(is_deleted=False)

    def deleted_set(self):
        queryset = NoDeleteQueryset(self.model, using=self._db)
        return queryset.filter(is_deleted=True)

    def all_with_deleted(self):
        return NoDeleteQueryset(self.model, using=self._db)
