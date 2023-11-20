
from ..modelFile.Reservation import Reservation, ReservationChat, ReservationChatPrivate, ReservationPayment, ReservationQualification
from rest_framework import serializers


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'idClient','idCompanyService','hourstart','hourFinish','observations','jsonUsersChat','state','created_at')
        read_only_fields = ('created_at',)

class ReservationChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationChat
        fields = ('id', 'idReservation','receiver','sender','message','state','created_at')
        read_only_fields = ('created_at',)


class ReservationPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationPayment
        fields = ('id', 'idReservation','idTypePay','value','nit','name','address','phone','email','created_at')
        read_only_fields = ('created_at',)

class ReservationQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationQualification
        fields = ('id', 'idReservation','idClient','qualification','observations','created_at')
        read_only_fields = ('created_at',)


class ReservationChatPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationChatPrivate
        fields = ('id', 'idReservation','receiver','sender','message','state','created_at')
        read_only_fields = ('created_at',)