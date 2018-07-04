from django.db import models
from django.contrib.auth.models import User

class PrayerType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Request(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    is_public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(null=True)
    scheduled_for = models.DateTimeField(null=True)
    prayer_type = models.ForeignKey(PrayerType, related_name='requests', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='requests', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



