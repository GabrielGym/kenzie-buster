from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)

    username = serializers.CharField(max_length=102, validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    password = serializers.CharField(max_length=127, write_only=True)
    is_superuser = serializers.BooleanField(default=False)
    

    def create(self, validated_data: dict) -> User:
        validated_data["is_superuser"] = validated_data["is_employee"]

        if validated_data.get("is_superuser"):
            return User.objects.create_superuser(**validated_data)
        
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        instance.is_employee = validated_data.get("is_employee", instance.is_employee)
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.is_superuser = validated_data.get("is_employee", instance.is_employee)
        instance.set_password(validated_data["password"]) 
        
        try: 
            instance.set_password(validated_data["password"]) 
            instance.save() 
        except KeyError: instance.save()

        return instance
    
class LoginSerialize(serializers.Serializer):
    username = serializers.CharField(max_length=102, write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)