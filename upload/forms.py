#ERROR DATE FORMAT ADMIN IS DIFFERENT WITH FRONT END

from django import forms
from django.forms import ModelForm
from upload.models import UploadActivity

from django.contrib.auth.models import User #for user import


# this cals is to show the DateInput field in template
class DateInput(forms.DateInput):
    input_type = 'date'

# Create the form class.
class UploadActivityForm(ModelForm):
	
	class Meta:
		model = UploadActivity
		fields = [
		'name',
		'project_name',
		'employee_name',
		'hours_worked',
		'activities_performed',
		'date',
		'image_1',
		'image_1_comments',
		'image_2',
		'image_2_comments',
		'image_3',
		'image_3_comments',
		'image_4',
		'image_4_comments',
		]
		widgets = {
			'date': DateInput(),
		}

# alternative way remove class DateInput + replace -> widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

# Creating a form to change an existing article.
#article = Article.objects.get(pk=1)
#form = ArticleForm(instance=article)
#https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/

	# project_name = models.ForeignKey('CreateProject', on_delete = models.CASCADE, null=True)
	# employee_name = models.ForeignKey('CreateEmployee', on_delete = models.CASCADE, null=True)
	# hours_worked = models.IntegerField(null=True, blank=True)
	# activities_performed = models.CharField(max_length=264, null=True, blank=False)
	# date = models.DateField(auto_now=False, null=True, blank=False)
	# date_created_system = models.DateTimeField(auto_now_add=True,null=True) #check this one is it correct and functional
	# image_1 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	# image_1_comments = models.CharField(max_length=264, null=True, blank=True)
	# image_2 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	# image_2_comments = models.CharField(max_length=264, null=True, blank=True)
	# image_3 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	# image_3_comments = models.CharField(max_length=264, null=True, blank=True)
	# image_4 = models.ImageField(upload_to='activity_fotos', null=True, blank=True)
	# image_4_comments = models.CharField(max_length=264, null=True, blank=True)
