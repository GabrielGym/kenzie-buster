from rest_framework import permissions
from rest_framework.views import Request, View

class isAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )
    
class isAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )

