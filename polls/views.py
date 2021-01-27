from django.http import HttpResponse
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics
from django.contrib.auth.models import User
from polls.serializers import ZolnierzSerializer, ZolnierzModelSerializer, KontraktySerializer, EkwipunekSerializer, PrzepustkiSerializer, WnioskiSerializer, Wyjazdy_sluzboweSerializer
from polls.models import Zolnierz, Kontrakty, Ekwipunek, Przepustki, Wnioski, Wyjazdy_sluzbowe
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ZolnierzList(generics.ListAPIView):
    queryset = Zolnierz.objects.all()
    serializer_class = ZolnierzModelSerializer
    permission_classes = []
    authentication_classes = []


class ZolnierzListCreate(generics.ListCreateAPIView):
    queryset = Zolnierz.objects.all()
    serializer_class = ZolnierzSerializer
    permission_classes = []
    authentication_classes = []


class KontraktyListCreate(generics.ListCreateAPIView):
    queryset = Kontrakty.objects.all()
    serializer_class = KontraktySerializer
    permission_classes = []
    authentication_classes = []
