from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GreetingSerializer
from .models import Greeting
from rest_framework.generics import GenericAPIView


class GreetingView(GenericAPIView):
    serializer_class =  GreetingSerializer
    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self,*args, **kwargs):
        last_greeting_value = ''
        greeting = Greeting.objects.latest('created_at')
        if greeting.body and len(greeting.body.split(" ")) > 1:
            last_greeting_value = greeting.body.split(" ")[len(greeting.body.split(" "))-1]
        else:
            last_greeting_value = greeting.body
        context = {'greeting': greeting, 'last_greeting_value': last_greeting_value}
        return render(self.request, 'greetings/index.html', context)

