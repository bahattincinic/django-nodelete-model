from django.db.models import query
from django.utils import timezone


class NoDeleteQueryset(query.QuerySet):
    def delete(self, hard=False):
        if hard:
            return super(NoDeleteQueryset, self).delete()
        return super(NoDeleteQueryset, self).update(is_deleted=True,
                                                    deleted_at=timezone.now())

    def hard_delete(self):
        return super(NoDeleteQueryset, self).delete()
