from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tigerapi.models import Frequency

class FrequencyView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for a single frequency

        Returns:
            Response -- JSON serialized frequency
        """
        try:
            frequency = Frequency.objects.get(pk=pk)
            serializer = FrequencySerializer(frequency)
            return Response(serializer.data)
        except Frequency.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all frequencies

        Returns:
            Response -- JSON serialized list of frequencies
        """
        frequencies = Frequency.objects.all()
        serializer = FrequencySerializer(frequencies, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for frequency
      
        Returns:
            Response -- JSON serialized frequency
        """

        frequency = Frequency.objects.create(
        habit_status=request.data["status"],
        habit_occurred=request.data["occurred"],
        notes=request.data["notes"],
        )
        serializer = FrequencySerializer(frequency)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a frequency

        Returns:
        Response -- Empty body with 204 status code
        """

        frequency = Frequency.objects.get(pk=pk)
        frequency.habit_status=request.data["status"]
        frequency. habit_occurred=request.data["occurred"]
        frequency.notes=request.data["notes"]
        frequency.save()
        serializer = FrequencySerializer(frequency)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        frequency=Frequency.objects.get(pk=pk)
        frequency.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class FrequencySerializer(serializers.ModelSerializer):
    """JSON serializer for frequency
    """
    class Meta:
        model = Frequency
        fields = ('id', 'habit_status', 'habit_occurred', 'notes', 'created_at', 'updated_at')
        depth = 1
