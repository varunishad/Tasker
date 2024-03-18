# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponseNotAllowed
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        if 'status' not in self.request.data:
            request.data['status'] = 'TO_DO'  # Set status to TO_DO bydefault if not provided

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer





# @csrf_exempt
# def create_task(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         title = data.get('title')
#         description = data.get('description', '')
#         status = data.get('status', 'To Do')
#         if title:
#             task = Task.objects.create(title=title, description=description, status=status)
#             return JsonResponse({id:task.id}, status=drf_status.HTTP_201_CREATED)
#         else:
#             return JsonResponse({'error':'Title is required'}, status=drf_status.HTTP_400_BAD_REQUEST)
#     else:
#         return HttpResponseNotAllowed(['POST'])


