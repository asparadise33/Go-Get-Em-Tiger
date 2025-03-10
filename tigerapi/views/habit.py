from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tigerapi.models import Habit, User, HabitTitle, Frequency, Category

class HabitView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for a single Habit

        Returns:
            Response -- JSON serialized Habit
        """
        try:
            habit= Habit.objects.get(pk=pk)
            categories = Category.objects.filter(categoryhabit__id=habit.id)
            habit.categories=categories
            serializer = HabitCategorySerializer(habit)
            return Response(serializer.data)
        except Habit.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all Habits

        Returns:
            Response -- JSON serialized list of Habits
        """
        habits= Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for Habit
      
        Returns:
            Response -- JSON serialized Habit
        """
        user = User.objects.get(pk=request.data["user_id"])
        habititle = HabitTitle.objects.get(pk=request.data["habititle_id"])
        frequency = Frequency.objects.get(pk=request.data["frequency_id"])

        habit = Habit.objects.create(
        user=user,
        habititle=habititle,
        frequency=frequency,
        notes=request.data["notes"]
        )
        serializer = HabitSerializer(habit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a Habit

        Returns:
        Response -- Empty body with 204 status code
        """
        user = User.objects.get(pk=request.data["user_id"])
        habititle = HabitTitle.objects.get(pk=request.data["habititle_id"])
        frequency = Frequency.objects.get(pk=request.data["frequency_id"])

        habit = Habit.objects.get(pk=pk)
        habit.user=user
        habit.habititle=habititle
        habit.frequency=frequency
        habit.notes=request.data["notes"]
        habit.save()
        serializer = HabitSerializer(habit)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        category=Habit.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for User
    """
    class Meta:
        model = User
        fields = ('id', 'user_name', 'bio')
        depth = 1
class HabitTitleSerializer(serializers.ModelSerializer):
    """JSON serializer for titles
    """
    class Meta:
        model = HabitTitle
        fields = ('id', 'habit_name')
        depth = 1
class FrequencySerializer(serializers.ModelSerializer):
    """JSON serializer for frequency
    """
    class Meta:
        model = Frequency
        fields = ('id', 'habit_status', 'habit_occurred', 'notes')
        depth = 1

class HabitSerializer(serializers.ModelSerializer):
    """JSON serializer for Habit
    """
    user= UserSerializer()
    habititle= HabitTitleSerializer()
    frequency=FrequencySerializer()
    class Meta:
        model = Habit
        fields = ('id', 'user', "habititle", 'frequency', 'notes', 'created_at', 'updated_at')
        depth = 4

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'name_of_category')

class HabitCategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    user= UserSerializer()
    habititle= HabitTitleSerializer()
    frequency=FrequencySerializer()
    class Meta:
        model = Habit
        fields = ('id', 'user', "habititle", 'frequency', 'notes', 'categories', 'created_at', 'updated_at')
        depth = 2
