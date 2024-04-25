from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)
    
    class Meta:
        model = ToDo
        fields = [
            'id',
            'description', 
            'status',
            'user_id'
        ]
        depth = 1
        extra_kwargs = {'user_id': {'read_only': True}}