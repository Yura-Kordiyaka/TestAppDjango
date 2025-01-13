from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import CustomUser
from .serializers import UserCreateSerializer

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    @extend_schema(
        summary="Register a new user",
        description="This endpoint allows anyone to register a new user. The request body must contain the required fields as defined in the UserCreateSerializer.",
        request=UserCreateSerializer,
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                response=UserCreateSerializer,
                description="User registration was successful."
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="The request body is invalid or missing required fields."
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
