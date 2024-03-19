from django.shortcuts import render,get_object_or_404,Http404
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  LeaveForm,StudentProfileForm,TeacherForm
from .models import  Student,LeaveRequest,Teacher
from django.contrib import messages

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

# About View
def about_view(request):
    return render(request, 'about.html')

# Contact View
def contact_view(request):
    return render(request, 'contact.html')

def student(request):
    return render(request,"student.html")

def courses(request):
    return render(request, 'courses.html')

def studentlogin(request):
    return render(request,"student_login.html")


def studentlog(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr=Student.objects.filter(username=username,password=password)
        e="error credentials"
        if cr:
            user_details=Student.objects.get(username=username,password=password)

            # for session
            id=user_details.id
            name=user_details.student_name
            department=user_details.department
            username=user_details.username

            request.session['id']=id
            request.session['name']=name
            request.session['department']=department
            request.session['username']=username


            return redirect('studentprofile')
        else:
            return render(request,'student_login.html',{'e':e})
        
    else:
        return render(request,'student_login.html')
    
def studentprofile(request):
    id=request.session['id']
    name=request.session['name']
    department=request.session['department']
    username=request.session['username']

    return render(request,"student_profile.html",{'id':id,'name':name,'department':department,"username":username})


# @login_required(login_url='/admin/login/')



def logout_view(request):
    logout(request)
    return redirect('/')

def leave(request):
    form=LeaveForm()
    if request.method=="POST":
        form=LeaveForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
        
    return render(request,"leave.html",{'form':form})

def index(request):
    return render(request,"index.html")


def layout(request):
    return render(request,"layout.html")

 
def update(request,pk):
    cr=Student.objects.get(id=pk)
    form2=StudentProfileForm(instance=cr)
    if request.method =="POST":
        form2=StudentProfileForm(request.POST,instance=cr)
        if form2.is_valid:
            form2.save()
            return redirect("studentprofile")
    return render(request,"update.html",{'form2':form2})

def leavestatus(request, pk):
    try:
        cl = LeaveRequest.objects.get(id=pk)
    except LeaveRequest.DoesNotExist:
        raise Http404("LeaveRequest does not exist")  # or return a custom error response
    return render(request, "leavestatus.html", {'cl': cl})


def teacher_reg(request):
    if request.method=="POST":
        t_username=request.POST.get('t_username')
        t_password=request.POST.get('t_password')
        t_name=request.POST.get('t_name')
        t_email=request.POST.get('t_email')
        t_department=request.POST.get('t_department')
        t_gender=request.POST.get('t_gender')
        Teacher(t_username=t_username, t_password=t_password,t_name=t_name,t_email=t_email,t_department=t_department,t_gender=t_gender).save()
    return render(request,'teacher_reg.html')

def t_log(request):
    return render(request,"teacher_login.html")

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            teacher = Teacher.objects.get(t_username=username)
            if teacher.t_password == password:
                if teacher.is_approval:
                    user_details=Teacher.objects.get(t_username=username,t_password=password)

                    # for session
                    id=user_details.id
                    t_name=user_details.t_name
                    t_email=user_details.t_email
                    t_department=user_details.t_department
                    t_username=user_details.t_username
                    t_number=user_details.t_number
                    t_gender=user_details.t_gender

                    request.session['id']=id
                    request.session['t_name']=t_name
                    request.session['t_email']=t_email
                    request.session['t_department']=t_department
                    request.session['t_username']=t_username
                    request.session['t_number']=t_number
                    request.session['t_gender']=t_gender
                # Redirect to teacher dashboard
                    return redirect('teacher_dashboard')
                else:
                # error page
                    return render(request, 't_error.html')
            
            else:
                return render(request, 'teacher_login.html', {'error': 'Invalid username or password.'})
    
        except Teacher.DoesNotExist:
            # Teacher with given username doesn't exist
            return render(request, 'teacher_login.html', {'error': 'Invalid username or password.'})
    
    return render(request, 'teacher_login.html')
 

def teacher_dashboard(request):
    id=request.session['id']

    t_name = request.session['t_name']
    t_email = request.session['t_email']
    t_department = request.session['t_department']
    t_username = request.session['t_username']
    t_number = request.session['t_number']
    t_gender = request.session['t_gender']
    if t_username:
        
        teacher = Teacher.objects.get(t_username=t_username)

        students = Student.objects.filter(department=teacher.t_department)
        leave_requests = LeaveRequest.objects.filter(student__department=teacher.t_department, status='Pending')

        return render(request, 'teacher_dashboard.html', {'id':id,'students': students, 'teacher': teacher, 'leave_requests': leave_requests,"t_name":t_name,"t_email":t_email,"t_department":t_department,"t_username":t_username,'t_number':t_number,'t_gender':t_gender})

    else:
        return redirect('t_login')


def update2(request,pk):
    cr=Teacher.objects.get(id=pk)
    form3=TeacherForm(instance=cr)
    if request.method =="POST":
        form3=TeacherForm(request.POST,instance=cr)
        if form3.is_valid:
            form3.save()
            return redirect("teacher_dashboard")
    return render(request,"update2.html",{'form3':form3})

def view_students(request):
    t_username = request.session.get('t_username')

    if t_username:
        
        teacher = Teacher.objects.get(t_username=t_username)

        students = Student.objects.filter(department=teacher.t_department)
        leave_requests = LeaveRequest.objects.filter(student__department=teacher.t_department, status='Pending')

        return render(request, 'view_students.html', {'students': students, 'teacher': teacher, 'leave_requests': leave_requests})

    else:
        return redirect('t_login')
    

def pending_requests(request):
    # Check if teacher is logged in
    t_username = request.session.get('t_username')
    if not t_username:
        messages.error(request, 'Teacher not found.')
        return redirect('t_login')

    try:
        # Get the teacher object
        teacher = Teacher.objects.get(t_username=t_username)
        # Filter leave requests for students of the same department with 'Pending' status
        pending_requests = LeaveRequest.objects.select_related('student').filter(student__department=teacher.t_department, status='PENDING')
    except Teacher.DoesNotExist:
        messages.error(request, 'Teacher not found.')
        return redirect('t_login')

    return render(request, 'pending_requests.html', {'teacher': teacher, 'pending_requests': pending_requests})

def logout_user(request):
    logout(request)
    return redirect('t_log')
   


def approve_leave(request, pk):
    student = get_object_or_404(Student, id=pk)
    leave_request = LeaveRequest.objects.filter(student=student, status='PENDING').first()

    if leave_request:
        leave_request.status = 'Approved'
        leave_request.save()

    return redirect('teacher_dashboard')


def t_error(request):
    return render(request,"t_error.html")

def view_student_request(request, pk):
    t_username = request.session.get('t_username')

    if t_username:
        teacher = Teacher.objects.get(t_username=t_username)
        student = get_object_or_404(Student, id=pk)
        leave_requests = LeaveRequest.objects.filter(student=student)
        
        return render(request, 'view_students2.html', {'teacher': teacher, 'student': student, 'leave_requests': leave_requests})

    else:
        return redirect('t_login')
