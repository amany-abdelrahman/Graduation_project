from .models import User
from rest_framework import serializers
class registeration(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all___'