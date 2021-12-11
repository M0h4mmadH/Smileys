from django.db import models
from django.utils import timezone

from users.models import User

class Request (models.Model):
    dcreator = User()
    reqID = models.IntegerField(default=0)
    createDate = models.DateTimeField(default = timezone.now())
    closeDate = models.DateTimeField(default = timezone.now())
    title = models.CharField(max_length=200,default='')
    description = models.CharField(max_length=1000,default='')
    image= models.CharField(max_length=200,default='')
    creator = models.ForeignKey(User,on_delete=models.DO_NOTHING, default=dcreator.pk)

    def __str__(self):
        return self.title+" - "+str(self.reqID)
