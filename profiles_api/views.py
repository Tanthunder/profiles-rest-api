from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
# status codes
from rest_framework import status
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
from rest_framework import filters


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete )',
            'It is similar to a traditional Django View',
            'Gives the most control over your application logic',
            'It is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self,request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})
        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating of object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return Hello message"""
        a_viewset = [
            'User actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functinality with less code',
        ]
        
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create Hello message"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk = None):
        """Handle getting an object by its iD"""
        return Response({'http_method':'Get'})
    
    def update(self, request, pk = None):
        """Handle updating an object by its iD"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk = None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk = None):
        """Removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)