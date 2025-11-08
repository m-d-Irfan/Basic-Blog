from django.db import models

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    parent  = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name