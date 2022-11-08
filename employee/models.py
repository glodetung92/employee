from django.db import models

# Create your models here.
class Employee(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Profile(models.Model):
	employee = models.ForeignKey(
		Employee,
		on_delete=models.CASCADE,
	)
	email = models.CharField(max_length=100)
	age = models.IntegerField()
	phone = models.CharField(max_length=11)
	address = models.CharField(max_length=200)

	def __str__(self):
		return self.email

