from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Django!"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employees_by_company(request, company):
    employees = Employee.objects.filter(company=company)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_employee(request, id):
    print("API HIT")
    try: 
        employee = Employee.objects.get(id=id)
        print(employee)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status = 200)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id).delete()
        return Response({"message": "Employee deleted"}, status=200)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        print(employee)
        serializer = EmployeeSerializer(data = request.data, instance = employee)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response (serializer.errors, status = 400)
    except Employee.DoesNotExist:
        return Response({"message": "Employee not found"}, status=404)
