from django.test import TestCase

from .models import Supplier


class ModelTestCase(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(name='Sony')

    def test_delete_model(self):
        self.supplier.delete()
        self.assertFalse(
            Supplier.objects.filter(id=self.supplier.id).exists())
