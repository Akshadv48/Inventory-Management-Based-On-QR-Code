import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Owner(models.Model):
	owner_id = models.IntegerField(default=0,primary_key=True)
	owner_Fname = models.CharField(max_length=200)
	owner_Lname = models.CharField(max_length=200)
	registered_date = models.DateTimeField('date added')

	def __str__(self):
		
		return str(self.owner_id)

	


class Installation(models.Model):
	owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
	installed_item = models.CharField(max_length=200)
	item_id = models.CharField(max_length=200)
	install_date = models.DateTimeField('date installed')
	
	def __str__(self):
		
		return str(self.owner_id)

class Maintainance(models.Model):
	owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
	maintain_item = models.CharField(max_length=200)
	item_id = models.CharField(max_length=200)
	maintain_date= models.DateTimeField('date Maintainance')
	Remarks = models.CharField(max_length=200)

	def __str__(self):
		#
		return str(self.owner_id)

