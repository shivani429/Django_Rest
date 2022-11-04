from urllib import request
from django.shortcuts import render  
from firstapp.serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
@api_view(['GET'])
def home(request):
    serializer_obj = student.objects.all()
    serializer = StudentSerializer(serializer_obj, many=True)
    return Response(serializer.data)

#CRUD OPERATIONS
#create
@api_view(['POST'])
def post_student(request):
    serializer_obj = student.objects.all()
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(['POST'])
def update_student(request,id):
    serializer_obj = student.objects.get(id=id)
    serializer = StudentSerializer(instance=serializer_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
def delete_student(request,id):
    serializer_obj = student.objects.get(id=id)
    serializer_obj.delete()
    return Response('student is deleted')

class studentlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class studentdisplay(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)

class studentlist(ListAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentcreate(CreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentup(UpdateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentrev(RetrieveAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentdel(DestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentlistCreate(ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentrevup(RetrieveUpdateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentrevdel(RetrieveDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentrevupdel(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentviewset(viewsets.ViewSet):
    def list(self,request):
        queryset = student.objects.all()
        serializer = StudentSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset = student.objects.get(id=id)
            serializer = StudentSerializer(queryset)
            return Response(serializer.data)

    def update(self,request,pk):
        id=pk
        queryset = student.objects.get(pk=id)
        serializer = StudentSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id=pk
        queryset = student.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'deleted'})

    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class studentviewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

        







