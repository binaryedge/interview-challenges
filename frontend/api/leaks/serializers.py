from rest_framework import serializers
from .models import DataLeak


class DataLeakSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataLeak
        fields = ('name',)
