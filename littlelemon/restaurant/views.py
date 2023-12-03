from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
