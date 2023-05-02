from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение всех пользователям
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить изменение/удаление только владельцам
        return obj.owner == request.user
