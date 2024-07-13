from App.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from App.models import *


# from rest_framework.validators import UniqueValidator
# from rest_framework_jwt.settings import api_settings



#______________DJANGO REACT AUTHENTICATION_________________

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email','phone', 'password')

#______________MWISHO HAPA DJANGO REACT AUTHENTICATION_________________





class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        # fields = ['id', 'username', 'email','phone','first_name','profile_image']












# kwa ajili ya kumregister mtu bila kutumia token
class UserCreationSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=25)
	email=serializers.EmailField(max_length=50)
	password=serializers.CharField(max_length=50)


	class Meta:
		model= MyUser
		fields= ['username','email','password']
		#fields='__all__'

	def validate(self,attrs):
		username_exists = MyUser.objects.filter(username=attrs['username']).exists()
		if username_exists:
			raise serializers.ValidationError(detail="User with username already exists")


		email_exists = MyUser.objects.filter(email=attrs['email']).exists()
		if email_exists:
			raise serializers.ValidationError(detail="User with email already exists")

		return super().validate(attrs)






class HudumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huduma
        fields = '__all__'

class MgawanjoWaHudumaSerializer(serializers.ModelSerializer):
    Category = HudumaSerializer(many=False)
    class Meta:
        model = MgawanjoWaHuduma
        fields = '__all__'


class UmriWaKukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmriWaKuku
        fields = '__all__'


class AinaZaKukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = AinaZaKuku
        fields = '__all__'

class UnitZaVyakulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitZaVyakula
        fields = '__all__'       


class VyakulaSerializer(serializers.ModelSerializer):
    Unit = UnitZaVyakulaSerializer(many=False)
    class Meta:
        model = Vyakula
        fields = '__all__'


class TaarifaZaKukuSerializer(serializers.ModelSerializer):
    AinaYaKuku = AinaZaKukuSerializer(many=False)
    UmriKwaWiki = UmriWaKukuSerializer(many=False)
    JinaLaChakula = VyakulaSerializer(many=False)
    class Meta:
        model = TaarifaZaKuku
        fields = '__all__'
