from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Burger", price=7)
        self.assertEqual(str(item), "Burger : 7")
