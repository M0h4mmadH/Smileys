from django.db import models

#from payments.models import Payment

class User(models.Model):
    #defaultPayment = Payment()
    userID = models.IntegerField(default=0)
    fname = models.CharField(max_length=500,default="")
    lname = models.CharField(max_length=500,default="")
    ability = models.CharField(max_length=500,default="")
    rate = models.IntegerField(default=0)
    phonenumber = models.CharField(max_length=50,default="")
    #payments = models.ForeignKey(Payment,on_delete=models.DO_NOTHING,default=defaultPayment)
    auth = models.BooleanField(default=True)

    #def __str__(self):
    #    return self.name+" - "+str(self.userID)

class Gift(models.Model):
    giftID = models.IntegerField(default=0)
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name+" - "+str(self.userID)

