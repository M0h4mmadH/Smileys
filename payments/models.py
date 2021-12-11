from django.db import models
from django.utils import timezone

from users.models import User

class Payment(models.Model):
    payID = models.IntegerField(default=0)
    date = models.DateTimeField('payment date', default=timezone.now())
    username = models.ForeignKey(User,on_delete=models.DO_NOTHING, default = User().pk)
    def __str__(self):
        return str(self.payID)
pass

class MoneyRequest(models.Model):
    amount = models.IntegerField(default=0)
