from django.shortcuts import render

from restaurant.serializers import UserSerializer, MenuSerializer
from django.contrib.auth.models import User
from .models import Booking, MenuItem
from .serializers import BookingSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

from .models import MenuItem

# Create your views here.
'''def index(request):
    return render(request, 'index.html', {})'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer