from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ContractSerializer, RoleSerializer, UsersSerializer, CompanySerializer, ServiceSerializer, TypePaySerializer, ReservationSerializer, AdministratorSerializer, CompanyAdressSerializer, CompanyPhonesSerializer, DocumentsUserSerializer, CompanyServicesSerializer, CompanyPicturesSerializer, ReservationChatSerializer, CompanyAdressHoursSerializer, ReservationPaymentSerializer, ReservationChatPrivateSerializer, ReservationQualificationSerializer

from .modelFile.Common import Contract,Role, TypePay
from .modelFile.Company  import Company, CompanyAdress, CompanyAdressHours, CompanyPhones, CompanyPictures, CompanyServices, Service
from .modelFile.Users import Administrator, DocumentsUser, Role, Users
from .modelFile.Reservation import Reservation, ReservationChat, ReservationChatPrivate, ReservationPayment, ReservationQualification


###IsAuthenticated
###IsAuthenticated
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContractSerializer

class TypePayViewSet(viewsets.ModelViewSet):
    queryset = TypePay.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TypePaySerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RoleSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer

class CompanyAdressViewSet(viewsets.ModelViewSet):
    queryset = CompanyAdress.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyAdressSerializer

class CompanyAdressHoursViewSet(viewsets.ModelViewSet):
    queryset = CompanyAdressHours.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyAdressHoursSerializer

class CompanyPhonesViewSet(viewsets.ModelViewSet):
    queryset = CompanyPhones.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyPhonesSerializer

class CompanyPicturesViewSet(viewsets.ModelViewSet):
    queryset = CompanyPictures.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyPicturesSerializer

class CompanyServicesViewSet(viewsets.ModelViewSet):
    queryset = CompanyServices.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyServicesSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer

class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AdministratorSerializer

class DocumentsUserViewSet(viewsets.ModelViewSet):
    queryset = DocumentsUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsUserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UsersSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationSerializer

class ReservationChatViewSet(viewsets.ModelViewSet):
    queryset = ReservationChat.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationChatSerializer

class ReservationChatPrivateViewSet(viewsets.ModelViewSet):
    queryset = ReservationChatPrivate.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationChatPrivateSerializer

class ReservationPaymentViewSet(viewsets.ModelViewSet):
    queryset = ReservationPayment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationPaymentSerializer

class ReservationQualificationViewSet(viewsets.ModelViewSet):
    queryset = ReservationQualification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationQualificationSerializer

