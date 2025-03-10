from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from tigerapi.models import HabitTitle
from tigerapi.views.habit_title import HabitTitleSerializer

class HabitTitleTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['habit_title']
    
    def setUp(self):
        
        self.habittitle = HabitTitle.objects.first()

    def test_create_title(self):
        """Create Habit Title Test"""
        url = "/habittitles"

        title = {
             "title":"test",
        }

        response = self.client.post(url, title, format='json')

        new_title = HabitTitle.objects.last()
        expected = HabitTitleSerializer(new_title)
        self.assertEqual(expected.data, response.data)

    def test_get_category(self):
        """Get Title Test
        """
        title= HabitTitle.objects.first()

        url = f'/habittitles/{title.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = HabitTitleSerializer(title)

        self.assertEqual(expected.data, response.data)  

    def test_list_titles(self):
        """Test list Titles"""
        url = '/habittitles'

        response = self.client.get(url)
        
        all_titles = HabitTitle.objects.all()
        expected = HabitTitleSerializer(all_titles, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data) 

    def test_update_title(self):
        """test update Title"""
      
        title = HabitTitle.objects.first()

        url = f'/habittitles/{title.id}'

        updated_title = {
            "title": f'{title.habit_name} updated',
        }
           

        response = self.client.put(url, updated_title, format='json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        title.refresh_from_db()

        self.assertEqual(updated_title['title'], title.habit_name)  
    
    def test_delete_title(self):
        """Delete Title Test"""
        title = HabitTitle.objects.first()
        url = f'/habittitles/{title.id}'
        
        response = self.client.delete(url)
        
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
