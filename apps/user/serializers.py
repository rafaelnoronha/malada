from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from .models import Usuario
from apps.core.decorators import fields_base_serializer


@fields_base_serializer
class UsuarioGetSerializer(serializers.ModelSerializer):

    def validate_password(self, password):
        validate_password(password)

        return make_password(password)

    class Meta:
        model = Usuario
        fields = [
            'id',
            'sr_name',
            'sr_email',
            'sr_observation',
            'sr_uuid_password_reset',
            'sr_type',

        ]
        read_only_fields = fields.copy()


class UsuarioListSerializer(UsuarioGetSerializer):
    pass


# class UsuarioPutPathSerializer(UsuarioGetSerializer):
#     groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True, required=True)

#     class Meta(UsuarioGetSerializer.Meta):
#         read_only_fields = [field for field in UsuarioGetSerializer.Meta.read_only_fields if field not in [
#             'email',
#             'groups',
#             'sr_nome',
#             'sr_telefone',
#             'sr_celular',
#         ]]


# class UsuarioPostSerializer(UsuarioGetSerializer):
#     groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True, required=True)

#     class Meta(UsuarioGetSerializer.Meta):
#         fields = UsuarioGetSerializer.Meta.fields.copy() + ['password',]
#         read_only_fields = [field for field in UsuarioGetSerializer.Meta.read_only_fields if field not in [
#             'username',
#             'email',
#             'password',
#             'is_staff',
#             'groups',
#             'sr_nome',
#             'sr_telefone',
#             'sr_celular',
#         ]]