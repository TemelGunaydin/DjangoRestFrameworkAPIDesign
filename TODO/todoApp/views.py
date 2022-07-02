from django.shortcuts import render
from .models import Todos
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Alttakini yazmadan Response alamadık
@api_view(['GET','POST'])
def todos(request,format=None):
    if request.method == 'GET':
        todos = Todos.objects.all()
        serializer = TodoSerializer(todos,many=True) 
        return Response(serializer.data)

    if request.method =='POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def todo_list(request,pk,format=None):
    try:
        todo = Todos.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer =TodoSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
