from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MenuViewTestCase(APITestCase):
    # Use the setup() method to set up the test case
    def setUp(self):
        self.data = {
            "id": 3,
			"title": "Ice Cream",
			"price": "5.50",
			"inventory": 100
		}
        self.token = "11744ab876e5b85944847a7296ffafe61bb1c0f2"
        
    # Test the GET request to the SingleMenuItemView APIView
    def test_get_request(self):
        headers = {'HTTP_AUTHORIZATION': 'Token ' + self.token}
        url = reverse('single_menu', args=[3])
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.data['title'])