from django.db import models

from users.models import User
from request.models import Request

class Charity(models.Model):
    charityID = models.IntegerField(default=0)
    name = models.CharField(max_length=500,default="")
    cardNumber = models.IntegerField(default=0)
    location = models.CharField(max_length=500,default="")
    phonenumber = models.CharField(max_length=500,default="")
    authusers = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=User().pk)
    reqs = models.ForeignKey(Request,on_delete=models.CASCADE,default=Request().pk)

    def __str__(self):
        return self.name+" - "+str(self.charityID)

    @property
    def showgifts(self):
        pass

