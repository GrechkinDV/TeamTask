from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from dry_rest_permissions.generics import DRYPermissions

from .models import Account
from .serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    permissions_classes = (DRYPermissions, )
    queryset = Account.objects.filter(is_active=True)
    http_method_names = ["get", "post", "patch", "delete"]

    def destroy(self, request, *args, **kwargs):
        """ Custom destroy method """
        account_object = self.get_object()
        account_object.is_active = False
        account_object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
