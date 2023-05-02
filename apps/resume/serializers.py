from rest_framework import serializers

from apps.resume.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    """Создаем сериализатор для модели Resume"""

    class Meta:  # Указываем мета-класс, определяющий параметры сериализатора
        model = Resume  # Указываем модель, которую нужно сериализовать
        fields = "__all__"  # Указываем поля, которые должны быть включены в сериализованный результат
        read_only_fields = (
            "id",
            "owner",
            "created_at",
        )  # Указываем поля, которые должны быть только для чтения
