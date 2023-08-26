from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=5.50, inventory=100)
        
    def test_get_item(self):
        item = Menu.objects.get(title="Ice Cream")
        self.assertEqual(item.title, "Ice Cream")
        
