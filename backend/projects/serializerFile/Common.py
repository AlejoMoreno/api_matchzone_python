from ..modelFile.Common import Contract,Role, TypePay
from rest_framework import serializers

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'paragraph','responsible','signature','created_at')
        read_only_fields = ('created_at',)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name','jsonPermissions','created_at')
        read_only_fields = ('created_at',)

class TypePaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePay
        fields = ('id', 'name','created_at')
        read_only_fields = ('created_at',)
