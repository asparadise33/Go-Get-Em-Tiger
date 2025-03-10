from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from tigerapi.models import Frequency
from tigerapi.views.frequency import FrequencySerializer

class FrequencyTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['frequency']
    
    def setUp(self):
        
        self.frequency = Frequency.objects.first()

    def test_create_frequency(self):
        """Create Frequency Test"""
        url = "/frequencies"

        frequency = {
             "status":"valid_choice",
             "occurred":"2025-03-05T14:30:00Z",
             "notes":"test",
        }

        response = self.client.post(url, frequency, format='json')

        new_frequency = Frequency.objects.last()
        expected = FrequencySerializer(new_frequency)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_frequency(self):
        """Get Frequency Test
        """
        frequency = Frequency.objects.first()

        url = f'/frequencies/{frequency.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = FrequencySerializer(frequency)

        self.assertEqual(expected.data, response.data)  

    def test_list_frequencies(self):
        """Test list Frequencies"""
        url = '/frequencies'

        response = self.client.get(url)
        
        all_frequencies = Frequency.objects.all()
        expected = FrequencySerializer(all_frequencies, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data) 

    def test_update_frequency(self):
        """test update Frequency"""
      
        frequency= Frequency.objects.first()

        url = f'/frequencies/{frequency.id}'

        updated_frequency = {
            "status": f'{frequency.habit_status} updated',
            "occurred": "2023-10-25T14:30:00+02:00",
            "notes": f'{frequency.notes} updated',
        }
           

        response = self.client.put(url, updated_frequency, format='json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        frequency.refresh_from_db()

        self.assertEqual(status.HTTP_200_OK, response.status_code) 
    
    def test_delete_frequency(self):
        """Delete FrequencyTest"""
        frequency = Frequency.objects.first()
        url = f'/frequencies/{frequency.id}'
        
        response = self.client.delete(url)
      
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
