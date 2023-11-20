from .serializerFile.Common import ContractSerializer, RoleSerializer, TypePaySerializer
from .serializerFile.Company import CompanySerializer, ProjectSerializer, CompanyAdressSerializer, CompanyPhonesSerializer, CompanyServicesSerializer, CompanyPicturesSerializer, CompanyAdressHoursSerializer, ServiceSerializer
from .serializerFile.Reservation import ReservationSerializer, ReservationChatSerializer, ReservationPaymentSerializer, ReservationChatPrivateSerializer, ReservationQualificationSerializer
from .serializerFile.Users import UsersSerializer, AdministratorSerializer, DocumentsUserSerializer

from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
