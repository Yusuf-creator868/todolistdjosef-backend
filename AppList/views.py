from django.shortcuts import render, redirect 
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SerializerTasks


from django.views.generic import TemplateView

class FrontendAppView(TemplateView):
    template_name = "index.html"

@api_view(["POST", "GET",])
def TasksCreate(request):
    if request.method == "POST":
        serializer = SerializerTasks(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("Incoming data:", request.data)
        return Response(serializer.errors, status=400)

    elif request.method == "GET":
            tasks = Task.objects.all().order_by("-id")
            serializer = SerializerTasks(tasks, many=True)
            return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



@api_view(['PATCH'])
def TaskUpdate(request, pk):
      task = Task.objects.get(id=pk)
      seriliazer = SerializerTasks(task, data = request.data)
      if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
      else:
        return Response(seriliazer.errors, status=status.HTTP_400_BAD_REQUEST)
      

# Create your views here.