from django.utils.decorators import method_decorator

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.resume.models import Resume
from apps.resume.serializers import ResumeSerializer
from apps.users.permissions import IsOwnerOrReadOnly


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Этот эндпоинт служит для просмотра всех резюме.",
        operation_summary="Просмотр всех резюме",
        tags=["Resume"],
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Этот эндпоинт служит для создании резюме.",
        operation_summary="Создание резюме",
        tags=["Resume"],
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Этот эндпоинт служит для просмотра определенного резюме.",
        operation_summary="Просмотр определенного резюме",
        tags=["Resume"],
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Этот эндпоинт служит для частичного обновления резюме.",
        operation_summary="Частичное обновление резюме",
        tags=["Resume"],
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Этот эндпоинт служит для обновления резюме.",
        operation_summary="Обновление резюме",
        tags=["Resume"],
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Этот эндпоинт служит для удаления резюме.",
        operation_summary="Удаление резюме",
        tags=["Resume"],
    ),
)
class ResumeViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Resume"""

    queryset = Resume.objects.all().prefetch_related("owner")
    serializer_class = ResumeSerializer
    filter_backends = (
        filters.SearchFilter,  # Фильтр поискавого запроса
        DjangoFilterBackend,  # Фильтрация данных на основе значений полей модели
        filters.OrderingFilter,  # Сортировка результатов запроса
    )
    search_fields = ("title", "grade")  # Поля по которым будет производится поиск
    filterset_fields = (
        "title",
        "experience",
        "status",
    )  # Поля по которым можно произвести фильтрацию
    ordering_fields = ("created_at",)  # Поля по которым можно произвести сортировку

    def get_permissions(self):
        """
        Метод для получения списка прав доступа для каждого действия.
        Если действие create, update, partial_update, destroy, то требуется
        аутентификация пользователя и проверка на владельца объекта.
        В ином случае разрешен доступ любому пользователю.
        """

        if self.action in ["create", "update", "partial_update", "destroy"]:
            composed_perm = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            composed_perm = [permissions.AllowAny]
        return [permission() for permission in composed_perm]

    def perform_create(self, serializer):
        """Метод для сохранения объекта Resume в БД с присвоением ему владельца."""
        serializer.save(owner=self.request.user)

    @swagger_auto_schema(
        operation_summary="Get all resume of current user",
        operation_description="The route is used to get all resume of current user",
        tags=["Resume"],
    )
    @action(detail=False, methods=["get"])
    def my(self, request):
        """Метод для получения списка резюме текущего пользователя"""
        queryset = Resume.objects.filter(owner=request.user.id)
        serializer = ResumeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
