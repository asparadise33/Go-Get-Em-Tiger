from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from tigerapi.models import Category
from tigerapi.views.category import CategorySerializer

class CategoryTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['category']
    
    def setUp(self):
        
        self.category = Category.objects.first()

    def test_create_category(self):
        """Create Category Test"""
        url = "/categories"

        category = {
             "category_name":"test",
        }

        response = self.client.post(url, category, format='json')

        new_category = Category.objects.last()
        expected = CategorySerializer(new_category)
        self.assertEqual(expected.data, response.data)

    def test_get_category(self):
        """Get Category Test
        """
        category= Category.objects.first()

        url = f'/categories/{category.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = CategorySerializer(category)

        self.assertEqual(expected.data, response.data)  

    def test_list_categories(self):
        """Test list Categories"""
        url = '/categories'

        response = self.client.get(url)
        
        all_categories = Category.objects.all()
        expected = CategorySerializer(all_categories, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data) 

    def test_update_user(self):
        """test update Category"""
      
        category= Category.objects.first()

        url = f'/categories/{category.id}'

        updated_category = {
            "category_name": f'{category.name_of_category} updated',
        }
           

        response = self.client.put(url, updated_category, format='json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        category.refresh_from_db()

        self.assertEqual(updated_category['category_name'], category.name_of_category)  
    
    def test_delete_user(self):
        """Delete Category Test"""
        category = Category.objects.first()
        url = f'/categories/{self.category.id}'
        
        response = self.client.delete(url)
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        exists = Category.objects.filter(id=self.category.id).exists()
        
        self.assertFalse(exists)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)  
