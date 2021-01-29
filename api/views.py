from django.shortcuts import render
from rest_framework import generics
from .custom_renderers import JPEGRenderer, PNGRenderer
from rest_framework.response import Response
from images.models import Image

# Create your views here.

class ImageAPIView(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Image.objects.get(id=self.kwargs['id']).image
        data = queryset
        # MIME type 'image/jpeg' is the valid option.
        return Response(data=data, content_type='image/jpeg')