from django.shortcuts import render

from restaurant.serializers import UserSerializer, MenuSerializer
from django.contrib.auth.models import User
from .models import Booking, MenuItem
from .serializers import BookingSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

#from rest_framework.permissions import IsAuthenticated

from .models import MenuItem

# Create your views here.
'''def index(request):
    return render(request, 'index.html', {})'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
@api_view()
@permission_classes([permissions.IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})