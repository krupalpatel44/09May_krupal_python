from django.shortcuts import render
from .serializer1 import *
from .models import *
from  rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getall(request):
    try:
        bdata=bookinfo.objects.all()
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serial=bookSerial(bdata,many=True)
    return Response(data=serial.data)


@api_view(['GET'])
def getid(request,id):
    try:
        bdata=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serial=bookSerial(bdata)
    return Response(data=serial.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=bookSerial(data=request.data)
        if serial.is_valid():
            serial.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def update(request,id):
    try:
        bkid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serial=bookSerial(bkid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=bookSerial(data=request.data,instance=bkid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def delete(request,id):
    try:
        bkid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serial=bookSerial(bkid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        bookinfo.delete(bkid)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)