from .models import Greeting
from rest_framework.serializers import ModelSerializer



class GreetingSerializer(ModelSerializer):
   
   class Meta:
       model = Greeting
       fields = '__all__'
