from django.db import models
from django.db.models import signals
from django.utils import timezone

from .managers import NoDeleteManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NoDeleteModel(BaseModel):
    is_deleted = models.BooleanField(default=False, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = NoDeleteManager()

    class Meta:
        abstract = True

    def delete(self, hard=False):
        if hard:
            return super(NoDeleteModel, self).delete()

        signals.pre_delete.send(
            sender=self.__class__,
            instance=self
        )

        self.is_deleted = True
        self.deleted_at = timezone.now()

        self.save()
        signals.post_delete.send(
            sender=self.__class__,
            instance=self
        )
