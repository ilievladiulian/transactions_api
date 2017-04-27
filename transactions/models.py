from django.db import models

# Create your models here.

class Transaction(models.Model):
	sender = models.IntegerField()
	receiver = models.IntegerField()
	amount = models.IntegerField()
	timestamp = models.DateField()