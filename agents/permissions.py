from rest_framework import permissions


class IsTeamLeaderOrAdminReadOnly(permissions.BasePermission):
    """
    Custom permission to identify TeamLeaders.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow admin user
        if request.user and request.user.is_staff:
            return True

        # Write permissions are only allowed to the user itself
        return obj == request.user
