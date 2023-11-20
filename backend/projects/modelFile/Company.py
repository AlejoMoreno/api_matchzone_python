from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sportType = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sportType = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Company(models.Model):
    name = models.TextField(max_length=200)
    nit = models.TextField(max_length=200)    
    slogan = models.TextField(max_length=200)
    icon = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


class CompanyPhones(models.Model):
    idCompany = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    phone = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class CompanyAdress(models.Model):
    idCompany = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    idCountry = models.TextField(max_length=200)
    idDepto = models.TextField(max_length=200)
    idCity = models.TextField(max_length=200)
    adress = models.TextField(max_length=200)
    grades = models.TextField(max_length=200)
    minutes = models.TextField(max_length=200)
    seconds = models.TextField(max_length=200) 
    open = models.BooleanField()
    description = models.TextField(max_length=900) 
    created_at = models.DateTimeField(auto_now_add=True)

class CompanyAdressHours(models.Model):
    idCompany = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    idCompanyAdress = models.ForeignKey(CompanyAdress, null=True, on_delete=models.CASCADE)
    monday = models.BooleanField()
    mondayStart = models.BigIntegerField(null=True)
    mondayFinish = models.BigIntegerField(null=True)
    tuesday = models.BooleanField()
    tuesdayStart = models.BigIntegerField(null=True)
    tuesdayFinish = models.BigIntegerField(null=True)
    wednesday = models.BooleanField()
    wednesdayStart = models.BigIntegerField(null=True)
    wednesdayFinish = models.BigIntegerField(null=True)
    thursday = models.BooleanField()
    thursdayStart = models.BigIntegerField(null=True)
    thursdayFinish = models.BigIntegerField(null=True)
    friday = models.BooleanField()
    fridayStart = models.BigIntegerField(null=True)
    fridayFinish = models.BigIntegerField(null=True)
    saturday = models.BooleanField()
    saturdayStart = models.BigIntegerField(null=True)
    saturdayFinish = models.BigIntegerField(null=True)
    sunday = models.BooleanField()
    sundayStart = models.BigIntegerField(null=True)
    sundayFinish = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CompanyServices(models.Model):
    idServices = models.ForeignKey(Service, null=True, on_delete=models.CASCADE)
    idCompanyAdressHours = models.ForeignKey(CompanyAdressHours, null=True, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    


class CompanyPictures(models.Model):
    idCompany = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    idCompanyAdress = models.ForeignKey(CompanyAdress, null=True, on_delete=models.CASCADE)
    picture = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
