from django.contrib import admin

from apps.resume.models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "specialty", "salary", "created_at")
    list_display_links = ("id", "title")
    search_fields = ("title", "owner", "specialty", "salary")
    list_filter = ("created_at", "specialty", "salary")
    empty_value_display = "-пусто-"
