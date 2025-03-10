from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from tigerapi.models import User
from tigerapi.views.user import UserSerializer

class UserTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['user']
    
    def setUp(self):
        
        self.user = User.objects.first()

    def test_create_user(self):
        """Create user test"""
        url = "/users"

        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        user = {
             "name":"test User",
             "bio":"test Bio"
        }

        response = self.client.post(url, user, format='json')

        new_user = User.objects.last()
        expected = UserSerializer(new_user)
        self.assertEqual(expected.data, response.data)

    def test_get_user(self):
        """Get user Test
        """
        user= User.objects.first()

        url = f'/users/{user.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = UserSerializer(user)

        self.assertEqual(expected.data, response.data)  

    def test_list_users(self):
        """Test list users"""
        url = '/users'

        response = self.client.get(url)
        
        all_users = User.objects.all()
        expected = UserSerializer(all_users, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data) 

    def test_update_user(self):
        """test update user"""
        # Grab the first game in the database
        user = User.objects.first()

        url = f'/users/{user.id}'

        updated_user = {
            "name": f'{user.user_name} updated',
            "bio": user.bio,
        }

        response = self.client.put(url, updated_user, format='json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        user.refresh_from_db()

        self.assertEqual(updated_user['name'], user.user_name)  
    
    def test_delete_user(self):
        """Delete User Test"""
        user = User.objects.first()
        url = f'/users/{self.user.id}'
        
        response = self.client.delete(url)
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        exists = User.objects.filter(id=self.user.id).exists()
        
        self.assertFalse(exists)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)        
