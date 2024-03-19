from django import forms
from .models import LeaveRequest, Student,Teacher

class LeaveForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ('student','description')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('t_name','t_username','t_department','t_number','t_email','t_gender')



class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'department','username'] # add other fields as needed
