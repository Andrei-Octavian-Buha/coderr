from rest_framework.urls import path
from .views import RegisterView

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='register')
]