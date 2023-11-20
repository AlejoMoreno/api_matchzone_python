from django.db import models
from .Company import Company
from .Common import Contract,Role
from django.contrib.auth.models import User


class Users(models.Model):
    username = models.TextField(max_length=200)
    email = models.EmailField()
    picture = models.ImageField(blank=True)
    password = models.TextField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)

class DocumentsUser(models.Model):
    idUser = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    document = models.ImageField()
    state = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class Administrator(models.Model):
    idCompany = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    idUser = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    idContract = models.ForeignKey(Contract, null=True, on_delete=models.CASCADE)
    idRole = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)