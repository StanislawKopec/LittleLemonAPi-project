from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.menu2 = Menu.objects.create(Title="Cake", Price=120, Inventory=50)
        self.url = '/restaurant/menu/items'

    def test_getall(self):
        response = self.client.get(self.url)
        
        expected_data = MenuSerializer([self.menu1, self.menu2], many=True).data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        self.assertEqual(response.data, expected_data)
