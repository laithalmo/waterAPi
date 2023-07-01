from django.db import models

# Create your models here.

class Daily(models.Model):

    numberofcups= models.IntegerField()
    numberofsleeping= models.IntegerField()

    # to do add user id
