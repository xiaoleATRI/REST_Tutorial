from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Customize permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read Permissions are allowed to any request
        # so we'll always allow GET, HEAD or Options requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to owner of the snippet.
        return obj.owner == request.user
