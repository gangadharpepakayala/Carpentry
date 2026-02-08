from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
	c = [
		('0','Guest'),
		('1','Customer'),
		('2','Admin'),
	]
	role_type = models.CharField(max_length=5,choices=c,default='0')
	mob = models.CharField(max_length=10)
	has_order = models.BooleanField(default=False)

class Order(models.Model):
	state = models.CharField(max_length=30)
	address =  models.CharField(max_length=100,null=True,blank=True)
	provide_wood = models.CharField(max_length=25)
	wood_type = models.CharField(max_length=25,blank=True)
	furniture_name = models.CharField(max_length=35)
	dimensions = models.CharField(max_length=20)
	img1 = models.ImageField(null=True,blank=True,upload_to='')
	img2 = models.ImageField(null=True,blank=True,upload_to='')
	o_stat = models.CharField(max_length=10,blank=True,default='None')
	cd = models.ForeignKey(User,on_delete=models.CASCADE)
	wood_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
	manfac_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
	m_time = models.DateField(default=None, null=True, blank=True)
	def __str__(request):
		
		return request.furniture_name+" - "+request.state


class Sell(models.Model):
	prdct_id = models.PositiveIntegerField(primary_key=True,blank=True)
	im1 = models.ImageField(null=True,blank=True,upload_to='')
	im2 = models.ImageField(null=True,blank=True,upload_to='')
	dim = models.CharField(max_length=20)
	wd_type = models.CharField(max_length=25,blank=True)
	f_name = models.CharField(max_length=35)
	o_price = models.CharField(max_length=10)
	c_price = models.CharField(max_length=10)
	s_stat = models.CharField(max_length=10,null=True)
	
class Payment(models.Model):
     c_name=models.CharField(max_length=35)
     c_number=models.CharField(max_length=12)
     c_expdate=models.CharField(max_length=5)
     c_cvv=models.CharField(max_length=3)
     cc=models.ForeignKey(User,on_delete=models.CASCADE)


