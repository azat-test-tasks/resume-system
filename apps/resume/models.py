from django.contrib.auth.models import User
from django.db import models


class Resume(models.Model):
    """Создаем модель Resume"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        blank=False,
        help_text="Заголовок резюме",
    )
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")
    specialty = models.CharField(max_length=100, verbose_name="Специальность")
    salary = models.IntegerField(verbose_name="Зарплата")
    education = models.TextField(verbose_name="Образование")
    status = models.CharField(max_length=100, verbose_name="Готовность к работе")
    grade = models.CharField(max_length=100, verbose_name="Квалификация")
    experience = models.TextField(verbose_name="Опыт работы")
    portfolio = models.URLField(
        verbose_name="Портфолио", blank=True, help_text="Ссылка на портфолио"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:  # строковое представление модели
        return self.title

    class Meta:  # Указываем мета-класс, определяющий параметры модели
        db_table = "resume"
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        indexes = [
            models.Index(fields=["owner", "specialty"]),
        ]
