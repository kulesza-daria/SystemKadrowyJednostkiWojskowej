from rest_framework import serializers
from datetime import date


class ZolnierzSerializer(serializers.Serializer):
    id_zolnierza = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=45, allow_null=False)
    nazwisko = serializers.CharField(max_length=45, allow_null=False)
    data_urodzenia = serializers.DateField(allow_null=False)
    telefon = serializers.CharField(max_length=15, allow_null=True)
    specjalnosc = serializers.CharField(max_length=90, allow_null=True)
    stanowisko_etatowe = serializers.CharField(max_length=90, allow_null=False)
    zameldowanie = serializers.CharField(max_length=200, allow_null=False)


class KontraktySerializer(serializers.Serializer):
    id_kontraktu = serializers.IntegerField(read_only=True)
    zolnierz = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    poczatek_kontraktu = serializers.DateField(allow_null=False)
    koniec_kontraktu = serializers.DateField(allow_null=False)
    wynagrodzenie = serializers.DecimalField(max_digits=9, decimal_places=2, default=3200, allow_null=False)


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
    data_zlozenia = serializers.CharField(max_length=45, default=date.today, allow_null=False)


class Wyjazdy_sluzboweSerializer(serializers.Serializer):
    id_wyjazdu = serializers.IntegerField(read_only=True)
    zolnierz = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    miejsce_docelowe = serializers.CharField(max_length=45, allow_null=False)
    cel = serializers.CharField(max_length=45, allow_null=False)
    data_wyjazdu = serializers.DateField(allow_null=False)
    data_przyjazdu = serializers.DateField(allow_null=False)
