from django.shortcuts import render, reverse
from api.models import VideoDetail
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from . import doc_serializer
from api.serializer import *
import math


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')


def validate_user(request):
    if request.method == 'POST' and request.is_ajax():
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        obj = authenticate(username=username, password=password)

        if obj:
            data = {'is_success': True}
            data.update({'url': reverse('api:index')})
            return JsonResponse(data, status=200)
        else:
            data = {'is_success': False}
            return JsonResponse(data, status=400)
    else:
        return JsonResponse({'error': 'Invalid Login Method'}, status=400)


class AddVideo(generics.GenericAPIView):

    serializer_class = doc_serializer.AddVideoSerializer

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            VideoDetail.add_detail(data)
            return Response({
                'message': 'Data has been Added successfully',
                'success': True,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Something went wrong. Exception: {}'.format(str(e)),
                'success': False,
            }, status=status.HTTP_404_NOT_FOUND)


class VideoDetailView(generics.GenericAPIView):

    serializer_class = doc_serializer.VideoDetailSerializer

    def post(self, request, *args, **kwargs):

        page_number = int(request.data['page'])
        page_size = 100
        offset = (page_number - 1) * page_size
        try:
            video = VideoDetail.objects.all()[offset: page_size + offset]
            count = VideoDetail.objects.all().count()
            total_pages = math.ceil(float(count) / page_size)
            serializer = VideoDetailSerializer(video, many=True)
            return Response({
                'message': 'Data has been fetched successfully',
                'success': True,
                'result': {
                    "videos": serializer.data,
                    "total_pages": total_pages
                }
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'message': 'Something went wrong. Exception: {}'.format(str(e)),
                'success': False,
                'result': {}
            }, status=status.HTTP_404_NOT_FOUND)