from datetime import date
from django.db import models


class Zolnierz(models.Model):
    id_zolnierza = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    data_urodzenia = models.DateField()
    telefon = models.CharField(max_length=15)
    specjalnosc = models.CharField(max_length=90)
    stanowisko_etatowe = models.CharField(max_length=90)
    zameldowanie = models.TextField(null=False)


class Kontrakty(models.Model):
    id_kontraktu = models.AutoField(primary_key=True)
    zolnierz = models.ForeignKey(Zolnierz, on_delete=models.CASCADE)
    poczatek_kontraktu = models.DateField(default=date.today, null=False)
    koniec_kontraktu = models.DateField(null=False)
    wynagrodzenie = models.DecimalField(max_digits=9, decimal_places=2, default=3200)


class Ekwipunek(models.Model):
    id_ekwipunku = models.AutoField(primary_key=True)
    zolnierz = models.ForeignKey(Zolnierz, on_delete=models.CASCADE)
    umundurowanie = models.CharField(max_length=45)
    uzbrojenie = models.CharField(max_length=45)
    oporzadzenie_uzbrojenia = models.CharField(max_length=45)


class Przepustki(models.Model):
    zolnierz = models.ForeignKey(Zolnierz, on_delete=models.CASCADE)
    poczatek_przepustki = models.DateField()
    koniec_przepustki = models.DateField()


class Wnioski(models.Model):
    id_wniosku = models.AutoField(primary_key=True)
    zolnierz = models.ForeignKey(Zolnierz, on_delete=models.CASCADE)
    rodzaj_wniosku = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    data_zlozenia = models.CharField(max_length=45, default=date.today, null=False)


class Wyjazdy_sluzbowe(models.Model):
    id_wyjazdu = models.AutoField(primary_key=True)
    zolnierz = models.ForeignKey(Zolnierz, on_delete=models.CASCADE)
    miejsce_docelowe = models.CharField(max_length=45, null=False)
    cel = models.CharField(max_length=45)
    data_wyjazdu = models.DateField()
    data_przyjazdu = models.DateField()
