from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email',)


class ModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = me
		fields = ('name',)