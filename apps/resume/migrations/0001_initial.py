# Generated by Django 4.2 on 2023-05-01 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Заголовок резюме",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
                ("email", models.EmailField(max_length=254, verbose_name="Почта")),
                (
                    "specialty",
                    models.CharField(max_length=100, verbose_name="Специальность"),
                ),
                ("salary", models.IntegerField(verbose_name="Зарплата")),
                ("education", models.TextField(verbose_name="Образование")),
                (
                    "status",
                    models.CharField(
                        max_length=100, verbose_name="Готовность к работе"
                    ),
                ),
                (
                    "grade",
                    models.CharField(max_length=100, verbose_name="Квалификация"),
                ),
                ("experience", models.TextField(verbose_name="Опыт работы")),
                (
                    "portfolio",
                    models.URLField(
                        blank=True,
                        help_text="Ссылка на портфолио",
                        verbose_name="Портфолио",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Резюме",
                "verbose_name_plural": "Резюме",
                "db_table": "resume",
            },
        ),
        migrations.AddIndex(
            model_name="resume",
            index=models.Index(
                fields=["owner", "specialty"], name="resume_owner_i_01b00e_idx"
            ),
        ),
    ]
