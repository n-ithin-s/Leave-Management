
from django.contrib import admin
from .models import LeaveRequest,Student,Teacher

# Register your models here.
admin.site.register(LeaveRequest)
admin.site.register(Student)
admin.site.register(Teacher)