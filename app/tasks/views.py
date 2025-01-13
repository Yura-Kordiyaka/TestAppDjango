from rest_framework import status, generics, response
from rest_framework.permissions import IsAuthenticated
from .permissions import TaskEditDestroyPermission
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter
from tasks.models import Task
from tasks.serializers import TaskSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiTypes


class CreateTaskApi(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @extend_schema(
        summary="Create a new task",
        description="This endpoint allows an authenticated user to create a new task. The request body must contain all required fields as defined in the TaskSerializer."
                    "The `status` field in the task can take the following values:\n"
                    "- `pending`: The task is not yet started.\n"
                    "- `in_progress`: The task is currently being worked on.\n"
                    "- `completed`: The task has been finished.\n",
        request=TaskSerializer,
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                response=TaskSerializer,
                description="The task was created successfully."
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="The request body is invalid or missing required fields."
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ListTaskApi(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    @extend_schema(
        summary="List all tasks",
        description="This endpoint allows an authenticated user to retrieve a list of all tasks. The response can be filtered using query parameters defined in TaskFilter.",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=TaskSerializer(many=True),
                description="A list of tasks."
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                description="Authentication credentials were not provided or are invalid."
            )
        },
        parameters=[
            OpenApiParameter(
                name='assigned_to_user',
                description='Filter tasks assigned to the currently authenticated user. Set to `true` to filter tasks assigned to the user.',
                required=False,
                type=OpenApiTypes.BOOL
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RetireUpdateDestroyTaskApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (TaskEditDestroyPermission,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @extend_schema(
        summary="Retrieve a task",
        description="This endpoint allows an authenticated user with appropriate permissions to retrieve a specific task by its ID.",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=TaskSerializer,
                description="The task was retrieved successfully."
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="The requested task does not exist."
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                description="Authentication credentials were not provided or are invalid."
            )
        },
        parameters=[
            OpenApiParameter(
                name='id',
                type=int,
                location='path',
                description='ID of the task to retrieve.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update a task",
        description=(
                "This endpoint allows an authenticated user with appropriate permissions to update a specific task. "
                "The task is identified by its ID and the request body must contain the updated task data. "
                "The `status` field in the task can take the following values:\n"
                "- `pending`: The task is not yet started.\n"
                "- `in_progress`: The task is currently being worked on.\n"
                "- `completed`: The task has been finished.\n"
                "Ensure that the request body contains one of these valid status values."
        ),
        request=TaskSerializer,
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=TaskSerializer,
                description="The task was updated successfully."
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Invalid data was provided for the update operation."
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="The requested task does not exist."
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                description="Authentication credentials were not provided or are invalid."
            )
        },
        parameters=[
            OpenApiParameter(
                name='id',
                type=int,
                location='path',
                description='ID of the task to update.'
            )
        ]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Partially update a task",
        description="This endpoint allows an authenticated user with appropriate permissions to partially update a specific task. The task is identified by its ID and the request body may contain only the fields to be updated."
                    "The `status` field in the task can take the following values:\n"
                    "- `pending`: The task is not yet started.\n"
                    "- `in_progress`: The task is currently being worked on.\n"
                    "- `completed`: The task has been finished.\n",
        request=TaskSerializer,
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=TaskSerializer,
                description="The task was partially updated successfully."
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Invalid data was provided for the update operation."
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="The requested task does not exist."
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                description="Authentication credentials were not provided or are invalid."
            )
        },
        parameters=[
            OpenApiParameter(
                name='id',
                type=int,
                location='path',
                description='ID of the task to partially update.'
            )
        ]
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a task",
        description="This endpoint allows an authenticated user with appropriate permissions to delete a specific task by its ID.",
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description="The task was deleted successfully."
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="The requested task does not exist."
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                description="Authentication credentials were not provided or are invalid."
            )
        },
        parameters=[
            OpenApiParameter(
                name='id',
                type=int,
                location='path',
                description='ID of the task to delete.'
            )
        ]

    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
