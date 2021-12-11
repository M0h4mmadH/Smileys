from django.db import models

from users.models import User
from request.models import Request

class Charity(models.Model):
    ID = models.IntegerField(default=0)
    name = models.CharField(max_length=500)
    cardNumber = models.IntegerField(default=0)
    location = models.CharField(max_length=500)
    phonenumber = models.CharField(max_length=500)
    authusers = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    reqs = models.ForeignKey(Request,on_delete=models.CASCADE)

    def __str__(self):
        return self.name+" - "+str(self.ID)

    @property
    def showgifts(self):
        pass

    #def acceptgift(self,gift Gift):
    #    pass
