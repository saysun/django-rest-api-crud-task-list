from rest_framework import serializers
from .models import Task


# this class converts Objects to Json

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('title', 'completed') # specify specific fields to serialize
        fields = '__all__'
