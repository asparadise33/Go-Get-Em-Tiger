from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tigerapi.models import Category

class CategoryView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for a single category

        Returns:
            Response -- JSON serialized category
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for category
      
        Returns:
            Response -- JSON serialized category
        """

        category = Category.objects.create(
        name_of_category=request.data["category_name"],
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
        Response -- Empty body with 204 status code
        """

        category = Category.objects.get(pk=pk)
        category.name_of_category=request.data["category_name"]
        category.save()
        serializer = CategorySerializer(category)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        category=Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'name_of_category', 'created_at', 'updated_at')
        depth = 1
