import os
from django.shortcuts import render
from rest_framework.views import APIView
from .renderers import ImageRenderer
from rest_framework.response import Response
from django.http import JsonResponse
from images.models import Image

# Create your views here.

ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']

class ImageAPIView(APIView):
    renderer_classes = [ImageRenderer]

    def get(self, request, *args, **kwargs):
        image = Image.objects.get(id=self.kwargs['id']).image
        base, ext = os.path.splitext(image.name)
        return Response(image, content_type='image/'+ext[1:])

    def post(self, request, *args, **kwargs):
        if 'image' in request.FILES:
            file = request.FILES['image']
            base, ext = os.path.splitext(file.name)
            if not ext in ALLOWED_IMAGE_EXTENSIONS:
                return JsonResponse({
                    'error': 'Invalid image file format.'
                }, status=400)
            obj = Image.objects.create(request.data)
            return JsonResponse({
                'status': 'added'
            }, status=201)