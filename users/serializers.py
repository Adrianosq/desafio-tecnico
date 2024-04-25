from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == 'password':

                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'is_admin',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message='A user with that username already exists.',
                    )
                ]
            },
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message='A user with this email already exists.',
                    )
                ]
            },
        }

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'is_admin']