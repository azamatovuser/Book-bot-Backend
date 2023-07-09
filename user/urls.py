from django.urls import path
from .views import UserListCreateAPIView, UserByWeekAPIView, UserByMonthAPIView


urlpatterns = [
    path('list_create/', UserListCreateAPIView.as_view()),
    path('statistic/week/', UserByWeekAPIView.as_view()),
    path('statistic/month/', UserByMonthAPIView.as_view()),
]