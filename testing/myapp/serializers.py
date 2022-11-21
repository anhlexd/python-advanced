from rest_framework import serializers
from myapp.models import TODOList

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODOList
        fields = (
            'id',
            'user',
            'title',
            'date_created',
            'date_modified'
        )
        read_only_fields = (
            'date_created',
            'date_modified'
        )