from django.db import models


class Contract(models.Model):
    paragraph = models.TextField(max_length=900)
    responsible = models.TextField(max_length=500)
    signature = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    name = models.TextField(max_length=500)
    jsonPermissions = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class TypePay(models.Model):
    name = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


