from rest_framework import routers
from django.contrib import admin
from .api import ContractViewSet, RoleViewSet, UsersViewSet, CompanyViewSet, ServiceViewSet, TypePayViewSet, ReservationViewSet, AdministratorViewSet
from .api import CompanyAdressViewSet, CompanyPhonesViewSet, DocumentsUserViewSet, CompanyPicturesViewSet, CompanyServicesViewSet, ReservationChatViewSet
from .api import CompanyAdressHoursViewSet, ReservationPaymentViewSet, ReservationChatPrivateViewSet, ReservationQualificationViewSet
from django.urls import path, include
from .views import LoginView, RegistrationView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register('contract', ContractViewSet, 'Contract')
router.register('role', RoleViewSet, 'Role')
router.register('users', UsersViewSet, 'Users')
router.register('company', CompanyViewSet, 'Company')
router.register('service', ServiceViewSet, 'Service')
router.register('typePay', TypePayViewSet, 'TypePay')
router.register('reservation', ReservationViewSet, 'Reservation')
router.register('administrator', AdministratorViewSet, 'Administrator')
router.register('companyAdress', CompanyAdressViewSet, 'CompanyAdress')
router.register('documentsUser', DocumentsUserViewSet, 'DocumentsUser')
router.register('companyPictures', CompanyPicturesViewSet, 'CompanyPictures')
router.register('companyServices', CompanyServicesViewSet, 'CompanyServices')
router.register('reservationChat', ReservationChatViewSet, 'ReservationChat')
router.register('companyPhones', CompanyPhonesViewSet, 'CompanyPhones')
router.register('companyAdressHours', CompanyAdressHoursViewSet, 'CompanyAdressHours')
router.register('reservationPayment', ReservationPaymentViewSet, 'ReservationPayment')
router.register('reservationChatPrivate', ReservationChatPrivateViewSet, 'ReservationChatPrivate')
router.register('reservationQualification', ReservationQualificationViewSet, 'ReservationQualification')

urlpatterns = [
     path('api/v-1/register/', RegistrationView.as_view(), name='user-registration'),
     path('api/v-1/login/', LoginView.as_view(), name='user-login'),
    path('api/v-1/token/', obtain_auth_token, name='api_token_auth'),
    path('api/v-1/admin/', include(router.urls)),
    path('api/v-1/auth/', admin.site.urls),
]