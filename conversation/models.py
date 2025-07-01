from django.db import models
from django.contrib.auth.models import User

class Converstaion(models.Model):
    item = models.ForeignK(Item, related_name='conversations', on_delete=model.CASCADE)
    member = models.ManyToManyField(User, related_name='converstaions')
    created_at = models.Date