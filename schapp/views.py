# views.py
# Design of HttpResponse object containing content of requested page

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from schapp.models import *
from schapp.serializers import *


# school list and detail
@api_view(['GET', 'POST'])
def school_list(request, format=None):
    """
    List all snippets or create a new film.
    """
    if request.method == 'GET':
        schools = School.objects.all()
        print('INFO: school_list')
        serializer = SchoolSerializer(schools, many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SchoolWriteSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# performance list and detail
@api_view(['GET', 'POST'])
def performance_list(request, format=None):
    """
    List all snippets or create a new film.
    """
    if request.method == 'GET':
        performances = Performance.objects.all()
        print('INFO: performance_list')
        serializer = PerformanceSerializer(performances, many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PerformanceWriteSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


