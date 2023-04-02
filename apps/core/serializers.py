from rest_framework import serializers

from .models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = [
            'active',
            'dma_created',
            'hms_created',
            'dma_alteration',
            'hms_alteration',
        ]
