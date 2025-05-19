from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from app.models import Task
from .serializers import TaskSerializer


class TaskAPI(APIView):
    """
    API view to handle CRUD Task for authenticated users.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Retrieve tasks",
        operation_description="Retrieve all tasks for the authenticated user. "
                              "If 'pk' is provided, retrieve a specific task.",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the task",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: TaskSerializer(many=True)}
    )
    def get(self, request, pk=None):
        """
        GET method to retrieve task(s).
        If `pk` is provided, fetch a single task.

        Parameters:
            request (HttpRequest): The incoming request.
            pk (int, optional): Primary key of the task to retrieve.

        Returns:
            Response: JSON representation of task(s).
        """
        if pk:
            task = get_object_or_404(Task, pk=pk, user=request.user)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            tasks = Task.objects.filter(user=request.user)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new task",
        operation_description="Create a task with authenticated user.",
        request_body=TaskSerializer,
        responses={
            201: TaskSerializer,
            400: 'Validation Error'
        }
    )
    def post(self, request):
        """
        POST method to create a new task.

        Parameters:
            request (HttpRequest): The request containing task data.

        Returns:
            Response: Created task data as JSON or validation errors.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing task",
        operation_description="Update a task with authenticated user.",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key task to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        request_body=TaskSerializer,
        responses={
            202: TaskSerializer,
            400: 'Validation Error'
        }
    )
    def put(self, request, pk):
        """
        PUT method to update a task.

        Parameters:
            request (HttpRequest): The incoming request.
            pk (int): Primary key of the task to update.
        Returns:
            Response: Updated task data or validation errors.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a task",
        operation_description="Delete a task with primary key of current user.",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the task to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={202: 'Task deleted successfully'}
    )
    def delete(self, request, pk):
        """
        DELETE method to remove a task.

        Parameters:
            request (HttpRequest): The incoming request.
            pk (int): Primary key of the task to delete.
        Returns:
            Response: Deleted task data or validation errors.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return Response({f'Successfully {pk} Deleted.'}, status=status.HTTP_202_ACCEPTED)
