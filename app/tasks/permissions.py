from rest_framework.permissions import BasePermission


class TaskEditDestroyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user and request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.created_by == request.user or request.user.is_superuser

        return True