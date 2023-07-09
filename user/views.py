from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from datetime import datetime, timedelta


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserByWeekAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        now = datetime.now()
        week_ago = now - timedelta(days=7)
        return qs.filter(created_date__range=(week_ago, now))


class UserByMonthAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        now = datetime.now()
        month_ago = now - timedelta(days=30)
        return qs.filter(created_date__range=(month_ago, now))