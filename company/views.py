from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import EmployeeSerializer


# this makes the view as a api view
# this way, you can use same url, with different methods


class EmployeeList(APIView):
    # getMethod
    @staticmethod
    def get(request):
        print('get with parameter: age')
        print(request.query_params.get('age'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    # Post Method
    @staticmethod
    def post(request):
        print('post data: ')
        print(request.data)
        Employee.objects.create(first_name='shaokang', last_name='zhanqing', employee_id=100)
        first_employee = Employee.objects.first()
        serializer = EmployeeSerializer(first_employee)
        return Response(serializer.data)
