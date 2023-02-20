from rest_framework import permissions

class IsSameUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj==request.user

class IsSameUserProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user==request.user