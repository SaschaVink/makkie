from django.contrib import admin
#from datetime import datetime # is this required here?

# Register your models here.
from upload.models import CreateProject
admin.site.register(CreateProject)

from upload.models import CreateEmployee
admin.site.register(CreateEmployee)

#from upload.models import UploadActivity (see below)
#admin.site.register(UploadActivity) (see below)

from upload.models import UploadActivity
class UploadActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created_system', 'id')
admin.site.register(UploadActivity, UploadActivityAdmin)



