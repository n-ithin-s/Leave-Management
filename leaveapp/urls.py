from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
  
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('studentlog/', views.studentlog, name='studentlog'),
    path('studentprofile/', views.studentprofile, name='studentprofile'),
    path('logout/', views.logout_view, name='logout'),
    path('leave/', views.leave, name='leave'),
    
    path('layout/', views.layout, name='layout'),
    path('update/<str:pk>',views.update,name="update"),
    path('leavestatus/<str:pk>',views.leavestatus,name="leavestatus"),
    path('teacher_reg/', views.teacher_reg, name='teacher_reg'),
    path('t_log/', views.t_log, name='t_log'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('view_students/', views.view_students, name='view_students'),
    path('pending_requests/', views.pending_requests, name='pending_requests'),
    path('teacher_logout/', views.logout_user, name='teacher_logout'),
    path('t_error/', views.t_error, name='t_error'),
    path('approve_leave/<str:pk>/', views.approve_leave, name='approve_leave'),
    path('update2/<str:pk>',views.update2,name="update2"),
    path('view_student_request/<str:pk>/', views.view_student_request, name='view_student_request'),


  
    # path('student-profile/', views.student_profile, name='student_profile'),
    # path('login/', views.login, name='login'),
    # path('loginuser/', views.login_user, name='loginuser'),
    # path('logout/', views.logout_view, name='logout'),
    # path('student_dashboard/', views.student_dashboard, name='student_dashboard')
]