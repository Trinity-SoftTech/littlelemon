from django.test import TestCase
from restaurant.models import Booking, MenuItem
from restaurant.serializers import MenuSerializer

from django.urls import reverse


class MenuViewTest(TestCase):
        
    def setUp(self):
            # Create a few Menu objects for testing
            MenuItem.objects.create(title="Pizza", price=9.99, inventory=10)
            MenuItem.objects.create(title="Pasta", price=7.99, inventory=15)
            MenuItem.objects.create(title="Salad", price=5.99, inventory=20)

    def test_get_all(self):
        """
        Test retrieving all Menu objects and compare with serialized data
        """
        # Assuming your list view is mapped to the name 'menu-list' in urls.py
        url = reverse("menu")

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)

        # Get all menus from db and serialize them
        menus = MenuItem.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that the API response matches the serialized data
        self.assertEqual(response.data, serializer.data)