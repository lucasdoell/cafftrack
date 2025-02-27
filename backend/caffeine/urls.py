from django.urls import path
from .views import CaffeineLogCreateAPIView, CaffeineLogListAPIView, CaffeineLogDetailAPIView, CaffeineOverTimeAPIView

urlpatterns = [
    path('logs/', CaffeineLogListAPIView.as_view(), name='caffeine-log-list'),  # List all logs
    path('logs/create/', CaffeineLogCreateAPIView.as_view(), name='caffeine-log-create'),  # Create log
    path('logs/<uuid:pk>/', CaffeineLogDetailAPIView.as_view(), name='caffeine-log-detail'),  # Retrieve single log by UUID
    path('caffeine-over-time/', CaffeineOverTimeAPIView.as_view(), name='caffeine-over-time'), 
]


