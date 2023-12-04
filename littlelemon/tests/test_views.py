from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):

        # Create few test instances of the Menu model.
        Menu.objects.create(title="Burger", price=7)
        Menu.objects.create(title="Pizza", price=12)

        # Create a test user.
        self.client = Client()
        self.user = User.objects.create_user(
            username = 'Adrian',
            password = 'password'
        )

        # Login with the test user.
        self.client.login(username = 'Adrian', password = 'password')

    def test_get_all(self):
        # Retreive objects of the Menu model.
        items = Menu.objects.all()

        # Serialize the objects of the Menu model.
        serialized_items = MenuSerializer(items, many=True)

        # Request objects of the Menu model.
        response = self.client.get('/restaurant/menu/')

        # Compare requested objeccts and serialized objects of the Menu model.
        self.assertEqual(response.data, serialized_items.data)
