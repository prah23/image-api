from django.urls import path, include
from .views import ImageAPIView

urlpatterns = [
    path('id/<id>/', ImageAPIView.as_view())
]
