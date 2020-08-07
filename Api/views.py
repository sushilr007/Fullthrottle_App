
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import base64
import io


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        text = "Welcome to first view port"
        return Response(text, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        return HttpResponse("Hello, world. You're at the polls index.")