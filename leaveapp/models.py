from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=200 , null=True)
    department = models.CharField(max_length=50, null=True)
    username=models.CharField(max_length=50, null=True)
    password=models.CharField(max_length=200,null=True)
    def __str__(self):
        return  self.student_name
    
    
    # add other student-related fields

class Teacher(models.Model):
    t_name = models.CharField(max_length=200, null=True)
    t_department = models.CharField(max_length=50, null=True)
    t_username= models.CharField(max_length=50, null=True)
    t_password= models.CharField(max_length=50, null=True)
    t_number=models.IntegerField( null=True)
    t_email= models.CharField(max_length=50, null=True)
    is_approval = models.BooleanField(default=False)  # Added the is_approval field
    gender_choices = [
    ('M', 'Male'),
    ('F', 'Female')
    ]
    t_gender = models.CharField(max_length=1, choices=gender_choices, null=True)  # Add gender field
    def __str__(self):
        return self.t_name


class LeaveRequest(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, null=True)
   
    status = models.CharField(max_length=20, default='PENDING')
    description = models.TextField()
    def __str__(self):
        return self.status
    

    
        
    # add other leave request fields
