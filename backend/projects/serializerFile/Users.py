from ..modelFile.Users import Administrator, DocumentsUser, Users
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username','email','picture','password','created_at')
        read_only_fields = ('created_at',)

class DocumentsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentsUser
        fields = ('id', 'idUser','document','state','created_at')
        read_only_fields = ('created_at',)

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id', 'idCompany','idUser','idContract','idRole','created_at')
        read_only_fields = ('created_at',)