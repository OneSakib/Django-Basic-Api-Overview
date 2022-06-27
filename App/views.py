from rest_framework import generics
from .models import Student
from .serializations import Student_serializer


# Create your views here.
class APICLASSVIEW(generics.ListCreateAPIView):
    serializer_class = Student_serializer
    queryset = Student.objects.all()


class APICLASSDDetailVIEW(generics.RetrieveUpdateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Student_serializer
    queryset = Student.objects.all()
