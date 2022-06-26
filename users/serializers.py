from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserRegisterSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)

        email = attrs.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError({'message': 'Email does exist!'})
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        user_obj = User(**validated_data)
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
