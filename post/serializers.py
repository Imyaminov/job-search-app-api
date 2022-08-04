from rest_framework import serializers
from common.models import User
from .models import Post, Status, Company, Statistic

class UserSerializers(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    class Meta():
        model = Company
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'

class StatisticSerializers(serializers.ModelSerializer):
    class Meta():
        model = Statistic
        fields = ['company_count', 'post_count', 'user_count']

