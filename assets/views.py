from django.http import JsonResponse
from .models import Asset
from .serializers import AssetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def asset_list(request, format=None):

    if request.method == 'GET':
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def asset_detail(request, id, format=None):
    
    try:
       asset = Asset.objects.get(pk=id)
    except Asset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssetSerializer(asset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
