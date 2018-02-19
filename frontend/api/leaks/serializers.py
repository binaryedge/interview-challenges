from rest_framework import serializers
from .models import DataLeak, DomainDataLeak, Email


class DataLeakSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataLeak
        fields = ('name',)


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = ('email',)


class DomainDataLeakSerializer(serializers.ModelSerializer):
    emails = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = DomainDataLeak
        fields = ('name', 'emails',)

    def get_name(self, obj):
        return obj.data_leak.name

    def get_emails(self, obj):
        serializer = EmailSerializer(obj.domain.email_set.all(), many=True)
        return serializer.data
