from rest_framework.permissions import BasePermission

import ads.models
from authentication.models import Profile


class AdsCreatePermission(BasePermission):
    message = "Added advertisements for non moderator or admin allowed."

    def has_permission(self, request, view):
        if request.user.role == Profile.MODERATOR:
            return True
        return False
