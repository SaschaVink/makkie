from django.shortcuts import render, redirect
from upload.models import UploadActivity
from upload.forms import UploadActivityForm # < here
from django.http import HttpResponseRedirect # < here what does it do???


from overview.filters import ProjectFilter #maybe create new filter in this app then change this

# Create your views here.


# is that initial stil required or can it be removed
def upload(request):
	if request.method == 'POST':
		form_upload_activity = UploadActivityForm(request.POST, request.FILES) 
		if form_upload_activity.is_valid():
			form_upload_activity.save()
			return HttpResponseRedirect('uploadoverview') #could replace this with redirect
	else:
		form_upload_activity = UploadActivityForm(initial={'date': 'Year-month-date'})
	return render(request, 'upload.html', {'form_upload_activity': form_upload_activity })


#change this form name as it's not readable but required to make it work as it's in the 
#template currently 14 is an ID that exists 
def updateactivity(request, pk):
 	update_activity = UploadActivity.objects.get(id=pk)
 	form_upload_activity = UploadActivityForm(instance=update_activity)
 	
 	if request.method == 'POST':
 		form_upload_activity = UploadActivityForm(request.POST, instance=update_activity)
 		if form_upload_activity.is_valid():
 			form_upload_activity.save()
 			return redirect('uploadoverview')



 	context = {'form_upload_activity': form_upload_activity}
 	return render(request, 'upload.html', context) 
 	form_upload_activity = UploadActivityForm(request.POST, instance=update_activity)




def uploadoverview(request):
	upload_activity = UploadActivity.objects.all()
	projectlist = UploadActivity.objects.all()
	projectfilter = ProjectFilter(request.GET, queryset=projectlist)
	context = {'upload_activity': upload_activity, 'projectfilter': projectfilter}
	return render(request, 'upload_overview.html', context)