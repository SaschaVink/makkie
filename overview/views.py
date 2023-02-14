from django.shortcuts import render
from upload.models import UploadActivity
from overview.filters import ProjectFilter 

#the below to imports are related to login and autenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.
#UploadActivity = UploadActivity.objects.all() #why not in the below code under def overview:
#projects = UploadActivity.objects.all()

@login_required
def overview(request):
	upload_activity = UploadActivity.objects.all()
	projectlist = UploadActivity.objects.all()
	projectfilter = ProjectFilter(request.GET, queryset=projectlist)
	context = {'upload_activity': upload_activity, 'projectfilter': projectfilter}
	return render(request, 'overview.html', context)

