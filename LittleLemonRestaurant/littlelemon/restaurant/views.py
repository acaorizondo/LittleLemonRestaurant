from django.shortcuts import render
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.contrib.auth.models import User
from . models import Booking, Menu
from . serializers import BookingSerializer, MenuSerializer, UserSerializer

# handle home page
def index(request):
    current_year = datetime.now().year
    context = {
        'current_year': current_year
    }
    return render(request, 'index.html', context)
@permission_classes([IsAuthenticated])
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
@permission_classes([IsAuthenticated]) 
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
@permission_classes([IsAuthenticated]) 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
# not used class implementation
""" 
class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) #Return data in JSON format
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Invalid data'},status=status.HTTP_400_BAD_REQUEST)

class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) #Return data in JSON format
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Invalid data'},status=status.HTTP_400_BAD_REQUEST)

"""

