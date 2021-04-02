
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from .custompermissions import MyPermission



class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes = [TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	#  authentication_classes = [BasicAuthentication]
	# permission_classes = [IsAdminUser]
	# permission_classes = [IsAuthenticatedOrReadOnly]
	# permission_classes = [DjangoModelPermissions]
	permission_classes = [IsAuthenticatedOrReadOnly]
