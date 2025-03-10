from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from tigerapi.models import Habit
from tigerapi.views.habit import HabitSerializer

class HabitTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['habit']
    
    def setUp(self):
        
        self.habit = Habit.objects.first()
 
    
    def test_get_habit(self):
        """Get habit Test
        """
        habit = Habit.objects.first()

        url = f'/habits/{habit.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected =HabitSerializer(habit)

        self.assertEqual(expected.data, response.data) 
