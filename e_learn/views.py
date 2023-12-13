from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
#from django.contrib.auth.models import User
from django.contrib.auth import login as authLogin, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
#from .models import Customer, Profile
# from .forms import TakeQuizForm, LearnerSignUpForm, InstructorSignUpForm, QuestionForm, BaseAnswerInlineFormSet, LearnerInterestsForm, LearnerCourse, UserForm, ProfileForm, PostForm
# from .forms import StudentSignUpForm, LecturerSignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.core import serializers
from django.conf import settings
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from datetime import datetime, date
from django.core.exceptions import ValidationError
from . import models
import operator
import itertools
from django.db.models import Avg, Count, Sum
from django.forms import inlineformset_factory
# from .models import TakenQuiz, Profile, Quiz, Question, Answer, Learner, User, Course, Tutorial, Notes, Announcement
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)

from django.contrib.auth import update_session_auth_hash           
# import cx_Oracle
from django.contrib.auth.models import User
from django.db import connection
from .models import *
from django.db.backends.signals import connection_created
import json
from django.db import connection

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

def home(request):
    return render(request, 'D:\MyUniversity\HK231\Informatio_Systems_Security\e_lms\e_learn\\templates\home.html')

from django.http import Http404

def courses(request):
    try:
        sv = Sinh_Vien.objects.get(mssv='1919856')
    except Sinh_Vien.DoesNotExist:
        raise Http404("Sinh_Vien does not exist")

    return render(request, 'your_template.html', {'student_info': sv})



def signup(request):
    return render(request, "signup-form.html")

def login_form(request):
    return render(request, 'login.html')

def set_student_role(**kwargs):
    connection = kwargs.get("connection", None)
    if connection:
        cursor = connection.cursor()
        cursor.execute("SET ROLE STUDENT IDENTIFIED BY %s", "pwd")

def set_teacher_role(**kwargs):
    connection = kwargs.get("connection", None)
    if connection:
        cursor = connection.cursor()
        cursor.execute("SET ROLE TEACHER IDENTIFIED BY %s", "pwd")

def set_admin_role(**kwargs):
    connection = kwargs.get("connection", None)
    if connection:
        cursor = connection.cursor()
        cursor.execute("SET ROLE ELEARNADM IDENTIFIED BY %s", "pwd")

def set_faculty_head_role(**kwargs):
    connection = kwargs.get("connection", None)
    if connection:
        cursor = connection.cursor()
        cursor.execute("SET ROLE falcuty_head IDENTIFIED BY %s", "pwd")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f'\n\n\n{email}\n\n\n\n')

        if email and email.endswith('@hcmut.st.edu.vn'):
            print(f'\n\nConnecting to student role....\n\n')
            connection_created.connect(set_student_role)
            username = email.strip('@')[0]
            user = User(username= username)
            print(f'\n\nStudent role connected\n\n')
            print(f'\n\nLogin successfuly\n\n')
            return redirect('student_home')
        # elif email and email.endswith('@hcmut.te.edu.vn'):
        #     print(f'\n\nConnecting to teacher role....\n\n')
        #     connection_created.connect(set_student_role)
        #     print(f'\n\nTeacher role connected\n\n')
        #     print(f'\n\nLogin successfuly\n\n')
        #     return redirect('home.html')
        elif email and email.endswith('@hcmut.ad.edu.vn'):
            print(f'\n\nConnecting to teacher role....\n\n')
            connection_created.connect(set_admin_role)
            print(f'\n\nAdmin role connected\n\n')
            print(f'\n\nLogin successfuly\n\n')
            return redirect('admin_dashboard')
        # elif email and email.endswith('@hcmut.fh.edu.vn'):
        #     print(f'\n\nConnecting to teacher role....\n\n')
        #     connection_created.connect(set_faculty_head_role)
        #     print(f'\n\nAdmin role connected\n\n')
        #     print(f'\n\nLogin successfuly\n\n')
        #     return redirect('home.html')
        else:
            messages.info(request, "Invalid Email or Password")
            return redirect('login')
    return render(request, 'login.html')

def student_dashboard(request):
    return render(request, 'dashboard\learner\home.html')

def student_course(request):
    if request.method == 'GET':
        mssv = request.GET.get('mssv')
        student_courses = Dang_Ky.objects.filter(mssv = mssv)

        print(student_courses)
        
        
def show_student():
    # Query to retrieve log entries
    query = "SELECT * FROM SINH_VIEN;"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        # Fetch all rows from the result set
        st = cursor.fetchall()

    context = {'student': st}
    return context
def get_all_student(request):
    list_sinh_vien = show_student()
    print(list_sinh_vien)
    return render(request, 'sinhvien.html', {'student': list_sinh_vien})
        
def admin_dashboard(request):
    return render(request, 'dashboard\\admin\home.html')

def get_audit_log(**kwargs):
    connection = kwargs.get("connection", None)
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT TIMESTAMP, DB_USER, OBJECT_NAME, POLICY_NAME, SQL_TEXT FROM  DBA_FGA_AUDIT_TRAIL;")
        audit_log_entries = cursor.fetchall()
        print(audit_log_entries)
        return(audit_log_entries)

def show_audit_log():
    # Query to retrieve log entries
    query = "SELECT TIMESTAMP, DB_USER, OBJECT_NAME, POLICY_NAME, SQL_TEXT FROM DBA_FGA_AUDIT_TRAIL"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        # Fetch all rows from the result set
        audit_log_entries = cursor.fetchall()

    context = {'audit_log_entries': audit_log_entries}
    return context

def audit_log(request):
    # log = get_audit_log()
    log = show_audit_log()
    print(log)
    return render(request, 'D:\MyUniversity\HK231\Informatio_Systems_Security\e_lms\e_learn\\templates\dashboard\\admin\log.html', log)
        