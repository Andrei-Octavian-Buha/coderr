from rest_framework import permissions

class IsCustomerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and
                     request.user.is_authenticated and 
                     request.user.profile.type== 'customer')
    
class IsOrderParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user == obj.customer_user or request.user == obj.business_user
        return request.user == obj.business_user