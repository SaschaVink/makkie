from django.db import models
from django.contrib.auth.models import User

# Create your models here
class CreateProject(models.Model):
	project_name = models.CharField(max_length=264, unique=True, null=True, blank=False)
	project_address = models.CharField(max_length=264, unique=False, null=True, blank=False)
	project_description = models.CharField(max_length=1000, null=True, blank=True)
	project_start_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	project_delivery_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

	def __str__(self):
		return self.project_name

#create a new app for the employer to create projects
#create a new app for the employer to create employees

class CreateEmployee(models.Model):
	employee_first_name = models.CharField(max_length=264, unique=False, null=True, blank=False)
	employee_last_name = models.CharField(max_length=264, unique=False, null=True, blank=False)
	employee_email = models.EmailField(max_length=264, unique=True, null=True, blank=True)
	employee_rate = models.PositiveIntegerField(null=True, blank=True)
	employee_description = models.CharField(max_length=264, unique=False)
	employee_own_bus = models.BooleanField(null=True, blank=True)
	employee_own_tool = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return self.employee_first_name + ' ' + self.employee_last_name

class UploadActivity(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	project_name = models.ForeignKey('CreateProject', on_delete=models.CASCADE, null=True)
	employee_name = models.ForeignKey('CreateEmployee', on_delete=models.CASCADE, null=True)
	hours_worked = models.IntegerField(null=True, blank=True)
	activities_performed = models.CharField(max_length=264, null=True, blank=False)
	date = models.DateField(auto_now=False, null=True, blank=False)
	date_created_system = models.DateTimeField(auto_now_add=True,null=True) #check this one is it correct and functional
	image_1 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	image_1_comments = models.CharField(max_length=264, null=True, blank=True)
	image_2 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	image_2_comments = models.CharField(max_length=264, null=True, blank=True)
	image_3 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	image_3_comments = models.CharField(max_length=264, null=True, blank=True)
	image_4 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	image_4_comments = models.CharField(max_length=264, null=True, blank=True)


	def __str__(self):
		return str(self.date) + ' ' + str(self.project_name) + ' ' + str(self.employee_name)

# Used date created in system as the redirect after upload form will go to the overview page
# The most recent created object then shows on top, please check with end user if this is desired
	class Meta:
		ordering = ['-date']
		verbose_name = 'Upload activity'
		verbose_name_plural = 'Upload activities'



