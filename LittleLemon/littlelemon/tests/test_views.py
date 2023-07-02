from django.test import TestCase, Client
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.icecream = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        menu = Menu.objects.all()
        response = self.client.get(reverse('menu'))
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
