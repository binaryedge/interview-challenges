from .models import Domain, Email
from .serializers import DataLeakSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class DomainDataLeaksViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        domain = request.GET.get('domain', '')
        domain = get_object_or_404(Domain.objects.all(), domain=domain)

        serializer = DataLeakSerializer([domaindataleak.data_leak for domaindataleak in domain.domaindataleak_set.all()], many=True)
        return Response(serializer.data)


class EmailDataLeaksViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        email = request.GET.get('email', '')
        email = get_object_or_404(Email.objects.all(), email=email)

        serializer = DataLeakSerializer([emaildataleak.data_leak for emaildataleak in email.emaildataleak_set.all()], many=True)
        return Response(serializer.data)

