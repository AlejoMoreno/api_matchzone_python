from django.db import models
from .Users import Users
from .Company import CompanyServices
from .Common import TypePay

class Reservation(models.Model):
    idClient = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    idCompanyService = models.ForeignKey(CompanyServices, null=True, on_delete=models.CASCADE)
    hourstart = models.DateTimeField()
    hourFinish = models.DateTimeField()
    observations = models.TextField(max_length=900)
    jsonUsersChat = models.JSONField()
    state = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReservationChat(models.Model):
    idReservation = models.ForeignKey(Reservation, null=True, on_delete=models.CASCADE)
    receiver = models.BigIntegerField()
    sender = models.BigIntegerField()
    message = models.TextField(max_length=500)
    state = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReservationPayment(models.Model):
    idReservation = models.ForeignKey(Reservation, null=True, on_delete=models.CASCADE)
    idTypePay = models.ForeignKey(TypePay, null=True, on_delete=models.CASCADE)
    value = models.FloatField()
    nit = models.TextField(max_length=500)
    name = models.TextField(max_length=500)
    address = models.TextField(max_length=500)
    phone = models.TextField(max_length=500)
    email = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class ReservationQualification(models.Model):
    idReservation = models.ForeignKey(Reservation, null=True, on_delete=models.CASCADE)
    idClient = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    qualification = models.BigIntegerField()
    observations = models.TextField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)

class ReservationChatPrivate(models.Model):
    idReservation = models.ForeignKey(Reservation, null=True, on_delete=models.CASCADE)
    receiver = models.BigIntegerField()
    sender = models.BigIntegerField()
    message = models.TextField(max_length=500)
    state = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)