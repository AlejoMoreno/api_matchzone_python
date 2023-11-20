from ..modelFile.Company  import Company, CompanyAdress, CompanyAdressHours, CompanyPhones, CompanyPictures, CompanyServices, Service, Project
from rest_framework import serializers



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title','description','sportType','created_at')
        read_only_fields = ('created_at',)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title','description','sportType','created_at')
        read_only_fields = ('created_at',)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name','nit','slogan','icon','created_at')
        read_only_fields = ('created_at',)

class CompanyPhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPhones
        fields = ('id', 'idCompany','phone','created_at')
        read_only_fields = ('created_at',)


class CompanyAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAdress
        fields = ('id', 'idCompany','idCountry','idDepto','idCity','adress','grades','minutes','seconds','open','created_at')
        read_only_fields = ('created_at',)


class CompanyAdressHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAdressHours
        fields = ('id', 'idCompany','idCompanyAdress','monday','mondayStart','mondayFinish','tuesday','tuesdayStart','tuesdayFinish','wednesday','wednesdayStart','wednesdayFinish','thursday','thursdayStart','thursdayFinish','friday','fridayStart','fridayFinish','saturday','saturdayStart','saturdayFinish','sunday','sundayStart','sundayFinish','created_at')
        read_only_fields = ('created_at',)

class CompanyServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyServices
        fields = ('id', 'idServices','idCompanyAdressHours','price','created_at')
        read_only_fields = ('created_at',)

class CompanyPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPictures
        fields = ('id', 'idCompany','idCompanyAdress','picture','created_at')
        read_only_fields = ('created_at',)
