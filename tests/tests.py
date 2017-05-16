from django.test import TestCase
from django.db.models import signals

from .models import Supplier


class ModelTestCase(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(name='Sony')

    def test_delete_model(self):
        self.supplier.delete()
        self.assertFalse(
            Supplier.objects.filter(id=self.supplier.id).exists()
        )

        self.assertTrue(
            Supplier.default_manager.filter(
                id=self.supplier.id,
                is_deleted=True,
                deleted_at__isnull=False).exists()
        )

    def test_signal(self):
        supplier = Supplier.objects.create(name='test')

        class PostDeleteHandler:
            def __init__(self):
                self.count = 0

            def __call__(self, signal, sender, instance, **kwargs):
                self.count += 1

        post_delete_handler = PostDeleteHandler()
        signals.post_delete.connect(post_delete_handler, weak=False)

        supplier.delete()
        self.supplier.delete()

        self.assertEqual(post_delete_handler.count, 2)

    def test_default(self):
        supplier = Supplier.objects.create(name='test')
        self.assertFalse(supplier.is_deleted)
        self.assertEqual(supplier.deleted_at, None)
        self.assertFalse(Supplier.objects.get(id=supplier.id).is_deleted)
        self.assertEqual(
            Supplier.objects.get(id=supplier.id).deleted_at, None)

    def test_hard_delete(self):
        supplier = Supplier.objects.create(name='test')
        supplier_id = supplier.id
        supplier.delete(hard=True)

        self.assertFalse(
            Supplier.objects.filter(id=supplier_id).exists()
        )

        self.assertFalse(
            Supplier.default_manager.filter(id=supplier_id).exists()
        )


class ManagerTestCase(TestCase):

    def test_get_queryset(self):
        Supplier.objects.create(name='queryset_1')
        Supplier.objects.create(name='queryset_1', is_deleted=True)

        self.assertEqual(
            Supplier.objects.filter(name__startswith='queryset').count(), 1
        )

    def test_deleted_set(self):
        Supplier.objects.create(name='deleted_set_1')
        Supplier.objects.create(name='deleted_set_2', is_deleted=True)
        Supplier.objects.create(name='deleted_set_3', is_deleted=True)

        self.assertEqual(
            Supplier.objects.deleted_set().filter(
                name__startswith='deleted_set').count(), 2
        )

    def test_all_with_deleted(self):
        Supplier.objects.create(name='all_with_deleted_1')
        Supplier.objects.create(name='all_with_deleted_2', is_deleted=True)
        Supplier.objects.create(name='all_with_deleted_3', is_deleted=True)

        self.assertEqual(
            Supplier.objects.all_with_deleted().filter(
                name__startswith='all_with_deleted').count(), 3
        )


class QuerysetTestCase(TestCase):

    def test_delete(self):
        Supplier.objects.create(name='queryset_1')

        self.assertEqual(
            Supplier.objects.filter(
                name__startswith='queryset').count(), 1
        )

        Supplier.objects.filter(name__startswith='queryset').delete()

        self.assertFalse(
            Supplier.objects.filter(name__startswith='queryset').exists()
        )

        self.assertTrue(
            Supplier.default_manager.filter(
                name__startswith='queryset').exists()
        )

    def test_delete_with_hard_param(self):
        Supplier.objects.create(name='queryset_hard_1')

        self.assertEqual(
            Supplier.objects.filter(
                name__startswith='queryset_hard').count(), 1
        )

        Supplier.objects.filter(
            name__startswith='queryset_hard').delete(hard=True)

        self.assertFalse(
            Supplier.objects.filter(
                name__startswith='queryset_hard').exists()
        )

        self.assertFalse(
            Supplier.default_manager.filter(
                name__startswith='queryset_hard').exists()
        )

    def test_hard_delete(self):
        Supplier.objects.create(name='hard_delete_1')

        self.assertEqual(
            Supplier.objects.filter(
                name__startswith='hard_delete').count(), 1
        )

        Supplier.objects.filter(
            name__startswith='hard_delete').hard_delete()

        self.assertFalse(
            Supplier.objects.filter(
                name__startswith='hard_delete').exists()
        )

        self.assertFalse(
            Supplier.default_manager.filter(
                name__startswith='hard_delete').exists()
        )
