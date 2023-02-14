import django_filters
from upload.models import UploadActivity
from django_filters.widgets import RangeWidget







# this way filtering works limited but seems to render better

class ProjectFilter(django_filters.FilterSet):
	date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

	class Meta:
		model = UploadActivity
		fields = {'project_name': ['exact'], 'employee_name':['exact']}



# this way filtering works but gives problems with adding classes 

#class ProjectFilter(django_filters.FilterSet):
#	class Meta:
#		model = UploadActivity
#		fields = {'project_name': ['exact'], 'employee_name':['exact'], 'date':['exact']}

# this way filtering works limited but seems to render better

# class ProjectFilter(django_filters.FilterSet):
# 	project_name = django_filters.CharFilter(lookup_expr='iexact')
# 	employee_name = django_filters.CharFilter(lookup_expr='iexact')
# 	date = django_filters.CharFilter(lookup_expr='iexact')
	
# 	class Meta:
# 		model = UploadActivity
# 		fields = {'project_name', 'employee_name', 'date'}



