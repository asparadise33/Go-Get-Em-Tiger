from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tigerapi.models import HabitTitle

class HabitTitleView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for a single title

        Returns:
            Response -- JSON serialized title
        """
        try:
            title = HabitTitle.objects.get(pk=pk)
            serializer = HabitTitleSerializer(title)
            return Response(serializer.data)
        except HabitTitle.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all titles

        Returns:
            Response -- JSON serialized list of titles
        """
        titles = HabitTitle.objects.all()
        serializer = HabitTitleSerializer(titles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for title
      
        Returns:
            Response -- JSON serialized title
        """

        title = HabitTitle.objects.create(
        habit_name=request.data["title"],
        )
        serializer = HabitTitleSerializer(title)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a title

        Returns:
        Response -- Empty body with 204 status code
        """

        title = HabitTitle.objects.get(pk=pk)
        title.habit_name=request.data["title"]
        title.save()
        serializer = HabitTitleSerializer(title)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        title = HabitTitle.objects.get(pk=pk)
        title.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class HabitTitleSerializer(serializers.ModelSerializer):
    """JSON serializer for titles
    """
    class Meta:
        model = HabitTitle
        fields = ('id', 'habit_name', 'created_at', 'updated_at')
        depth = 1
