from rest_framework import status
from rest_framework import authentication, exceptions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail, send_mass_mail
import datetime
import random
import speech_recognition as sr

def home(request,chat_room,user):
    return render(request, "prototype/proto.html")
# Create your views here.


class voice(APIView):
    parser_classes = [JSONParser]
    def get(self,request,chat_room,user):
        return Response({"list":Messages.objects.filter(chat_room=chat_room).values(),"user":user}, status=status.HTTP_200_OK)
    def post(self,request,chat_room,user):
        # Initialize the recognizer
        # print("hi")
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source)
        result = r.recognize_google(audio)
        m=Messages.objects.create(chat_room=chat_room,user=user,data=result)
        m.save()
        return Response({"detail":None}, status=status.HTTP_200_OK)