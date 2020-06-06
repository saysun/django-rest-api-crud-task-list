from rest_framework import serializers
from .models import Employee

# This serializes the Employee model to json
# specifies the specific fields or all fields to be serialized
#
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ('first_name', 'last_name')
        fields = '__all__'
