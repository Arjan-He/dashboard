from django.db import models

# Create your models here.
class StravaActivity(models.Model):
    """In deze klasse komen de activiteiten die gedownload worden van Strava"""
    strava_id=models.IntegerField(help_text='De Strava-id van de activiteit')
    naam = models.CharField(max_length=20, help_text='De omschrijving van de activiteit')
    startdatumtijd = models.DateTimeField(help_text='De lokale starttijd de activiteit')
    einddatumtijd = models.DateTimeField(help_text='De lokale eindtijd van de activiteit')
    type_activiteit = models.CharField(max_length=20, help_text='Het type van de activiteit')
    afstand = models.DecimalField(max_digits=6, decimal_places=1, help_text='De afgelegde afstand in meters')
    beweegtijd = models.IntegerField(help_text='De bewogen tijd in seconden')
    totaaltijd = models.IntegerField(help_text='De duur van de activiteit in seconden')
    externe_id = models.CharField(max_length=20, help_text='De id van de externe app (Garmin)')
    kudos_aantal = models.IntegerField(help_text='Het aantal ontvangen kudos')
    map_polyline = models.TextField(help_text='De gecodeerde polyline kaart in Google maps formaat')
