from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tigerapi.models import User

class UserView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for a single User

        Returns:
            Response -- JSON serialized User
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all Users

        Returns:
            Response -- JSON serialized list of Users
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for User
      
        Returns:
            Response -- JSON serialized User
        """

        user = User.objects.create(
        user_name=request.data["name"],
        bio=request.data["bio"],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a User

        Returns:
        Response -- Empty body with 204 status code
        """

        user = User.objects.get(pk=pk)
        user.user_name=request.data["name"]
        user.bio=request.data["bio"]
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        user=User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for User
    """
    class Meta:
        model = User
        fields = ('id', 'user_name', 'bio', 'created_at')
        depth = 1
