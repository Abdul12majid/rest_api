from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ModelSerializer
from django.contrib.auth.models import User
from .models import me

# Create your views here.

@api_view(['GET'])
def home(request):
	return Response('well well well')

@api_view(['POST','GET'])
def users(request):
	all_user = User.objects.all()
	serializer = UserSerializer(all_user, many=True)
	add_user = UserSerializer(data=request.data)
	if add_user.is_valid():
		add_user.save()
	return Response(serializer.data)