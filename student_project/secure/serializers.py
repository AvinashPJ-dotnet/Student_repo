from rest_framework import serializers
from . import models

class SecureSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Secure
        fields=(
            'id',
            'entity_id',
            'username',
            'password'
        )