from rest_framework import serializers
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as message
from polls.models import *


def validate(data):
    if data > date.today():
        raise ValidationError(
            message('%(data) data z przyszłości'),
            params={'value': data},
        )


class ZolnierzSerializer(serializers.Serializer):
    id_zolnierza = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=45, allow_null=False)
    nazwisko = serializers.CharField(max_length=45, allow_null=False)
    data_urodzenia = serializers.DateField(allow_null=False, validators=[validate])
    telefon = serializers.CharField(max_length=9, allow_null=True)
    specjalnosc = serializers.CharField(max_length=90, allow_null=True)
    stanowisko_etatowe = serializers.CharField(max_length=90, allow_null=False)
    zameldowanie = serializers.CharField(max_length=200, allow_null=False)

    def create(self, validated_data):
        return Zolnierz.objects.create(**validated_data)


class ZolnierzModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zolnierz
        fields = ('imie', 'nazwisko', 'wynagrodzenie')


class KontraktySerializer(serializers.Serializer):
    id_kontraktu = serializers.IntegerField(read_only=True)
    # zolnierz = serializers.PrimaryKeyRelatedField(many=False, allow_null=False)
    poczatek_kontraktu = serializers.DateField(allow_null=False)
    koniec_kontraktu = serializers.DateField(allow_null=False)
    wynagrodzenie = serializers.DecimalField(max_digits=9, decimal_places=2, default=3200, allow_null=False)

    def create(self, validated_data):
        return Kontrakty.objects.create(**validated_data)


class KontraktyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kontrakty
        fields = '__all__'


class EkwipunekSerializer(serializers.Serializer):
    id_ekwipunku = serializers.IntegerField(read_only=True)
    zolnierz = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    umundurowanie = serializers.CharField(max_length=45, allow_null=True)
    uzbrojenie = serializers.CharField(max_length=45, allow_null=True)
    oporzadzenie_uzbrojenia = serializers.CharField(max_length=45, allow_null=True)


class PrzepustkiSerializer(serializers.Serializer):
    zolnierz = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    poczatek_przepustki = serializers.DateField(allow_null=False)
    koniec_przepustki = serializers.DateField(allow_null=False)


class WnioskiSerializer(serializers.Serializer):
    id_wniosku = serializers.IntegerField(read_only=True)
    zolnierz = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    rodzaj_wniosku = serializers.CharField(max_length=45, allow_null=False)
    status = serializers.CharField(max_length=45, allow_null=False)
    data_zlozenia = serializers.DateField(allow_null=False)


class Wyjazdy_sluzboweSerializer(serializers.Serializer):
    id_wyjazdu = serializers.IntegerField(read_only=True)
    zolnierz = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    miejsce_docelowe = serializers.CharField(max_length=45, allow_null=False)
    cel = serializers.CharField(max_length=45, allow_null=False)
    data_wyjazdu = serializers.DateField(allow_null=False)
    data_przyjazdu = serializers.DateField(allow_null=False)
