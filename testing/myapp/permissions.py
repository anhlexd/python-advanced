from rest_framework import permissions

class IsOwnwe(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.id == obj.user_id