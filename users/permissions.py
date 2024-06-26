from rest_framework import permissions
from rest_framework.views import View, Request


class IsAuthorized(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        else:
            return request.user.is_authenticated 


class IsAuthorizedOrNot(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        if request.user.is_authenticated:
            if request.method == "PATCH":
                return obj.id == request.user.id
            else:
                return request.user.id == obj.id
        return False
