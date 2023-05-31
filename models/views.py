from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework import viewsets
from .serializers import shool_serializer
from models.models import shool

class Shool(APIView):
    @method_decorator(cache_page(60*60*2))
    def get(self, request, format=None):
        school_intern = shool.objects.all()
        serializer = shool_serializer(school_intern, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = shool_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        shool.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)