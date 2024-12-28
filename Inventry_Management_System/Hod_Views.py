from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#from app.models import *
from app.models import *
from django.contrib import messages
from django.http import HttpResponse

from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required(login_url='/')
def HOME(request):
    mgmt_count=Mgmt.objects.all().count()
    staff_count=Staff.objects.all().count()
    supplier_count=Supplier.objects.all().count()
    product_count=Product.objects.all().count()

    mgmt_gender_male=Mgmt.objects.filter(gender='Male').count()
    mgmt_gender_female=Mgmt.objects.filter(gender='Female').count()
    
    context={
        'mgmt_count':mgmt_count,
        'staff_count':staff_count,
        'supplier_count':supplier_count,
        'product_count':product_count,
        'mgmt_gender_male':mgmt_gender_male,
        'mgmt_gender_female':mgmt_gender_female,
    }
    return render(request,'Hod/home.html',context)     

#=========================Grade=========================
@login_required(login_url='/')
def ADD_GRADE(request):
    if request.method == "POST":
        grade_name = request.POST.get('grade_name')
        grade_salary = request.POST.get('grade_salary')
        grade_status = request.POST.get('grade_status')
        grade = Grade(
            name = grade_name,
            salary = grade_salary,
            status = grade_status,
        )
        grade.save()
        messages.success(request,'Grade is Successfully Created. ')
        
        return redirect('view_grade')
    return render(request,'Hod/add_grade.html')

@login_required(login_url='/')
def VIEW_GRADE(request):
    grade = Grade.objects.all()   
    context = {
        'grade':grade,       
    }
    return render(request,'Hod/view_grade.html',context)

@login_required(login_url='/')
def EDIT_GRADE(request,id):
    grade=Grade.objects.get(id=id)
    context={
        'grade':grade,
    }
    return render(request,'Hod/edit_grade.html',context)

@login_required(login_url='/')
def UPDATE_GRADE(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        salary=request.POST.get('salary')
        status=request.POST.get('status')
        grade_id=request.POST.get('grade_id')
        grade=Grade.objects.get(id=grade_id)
        grade.name=name
        grade.salary=salary
        grade.status=status
        grade.save()
        messages.success(request,'Grade is Successfully Updated.')
        return redirect('view_grade')
    return render(request,'Hod/edit_grade.html')  

@login_required(login_url='/')
def DELETE_GRADE(request, id):    
    grade = Grade.objects.get(id=id)
    grade.delete()
    return redirect('view_grade')    

#===========================Management====================
@login_required(login_url='/')
def ADD_MGMT(request):
    grade = Grade.objects.all()    

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        status = request.POST.get('status')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        grade_id = request.POST.get('grade_id')       

        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email is Already Used')
           return redirect('add_mgmt')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username is Already Used')
           return redirect('add_mgmt')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()

            grade = Grade.objects.get(id=grade_id)           

            mgmt = Mgmt(
                admin = user,
                address = address,
                mobile = mobile,
                status = status,             
                grade_id = grade, 
                gender = gender,
            )
            mgmt.save()
            messages.success(request, user.first_name + "  " + user.last_name + " is Successfully Added !")
            return redirect('view_mgmt')

    context = {
        'grade':grade,               
    }
    return render(request,'Hod/add_mgmt.html',context)

@login_required(login_url='/')
def VIEW_MGMT(request):
    mgmt=Mgmt.objects.all()
    context={
        'mgmt':mgmt,
    }
    return render (request, 'Hod/view_mgmt.html',context)

@login_required(login_url='/')
def EDIT_MGMT(request,id):
    mgmt=Mgmt.objects.filter(id=id)
    grade=Grade.objects.all()    

    context={
        'mgmt':mgmt,
        'grade':grade,       
    }
    return render(request,'HOD/edit_mgmt.html',context)

@login_required(login_url='/')
def UPDATE_MGMT(request):
    if request.method == "POST":
        mgmt_id = request.POST.get('mgmt_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        status = request.POST.get('status')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        grade_id = request.POST.get('grade_id')  

        user = CustomUser.objects.get(id = mgmt_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        mgmt = Mgmt.objects.get(admin = mgmt_id)
        mgmt.address = address
        mgmt.gender = gender
        mgmt.mobile = mobile
        mgmt.status = status
        
        grade = Grade.objects.get(id = grade_id)
        mgmt.grade_id = grade      
        mgmt.save()
        messages.success(request,'Record is Successfully Updated !')
        return redirect('view_mgmt')
    return render(request,'Hod/edit_mgmt.html')

@login_required(login_url='/')
def DELETE_MGMT(request,admin):
    mgmt = CustomUser.objects.get(id = admin)
    mgmt.delete()
    messages.success(request,'Record is Successfully Deleted !')
    return redirect('view_mgmt')

#===============================Staff=====================
@login_required(login_url='/')
def ADD_STAFF(request):
    grade = Grade.objects.all()    
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        status = request.POST.get('status')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        grade_id = request.POST.get('grade_id')       

        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email is Already Used')
           return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username is Already Used')
           return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            grade = Grade.objects.get(id=grade_id)           

            staff = Staff(
                admin = user,
                address = address,
                mobile = mobile,
                status = status,             
                grade_id = grade,
                gender = gender,
            )
            staff.save()
            messages.success(request, user.first_name + "  " + user.last_name + " is Successfully Added !")
            return redirect('view_staff')

    context = {
        'grade':grade,               
    }
    return render(request,'Hod/add_staff.html',context)

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff=Staff.objects.all()
    context={
        'staff':staff,
    }
    return render (request, 'Hod/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff=Staff.objects.filter(id=id)
    grade=Grade.objects.all()    

    context={
        'staff':staff,
        'grade':grade,       
    }
    return render(request,'HOD/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        status = request.POST.get('status')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        grade_id = request.POST.get('grade_id')  

        user = CustomUser.objects.get(id = staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        staff = Staff.objects.get(admin = staff_id)
        staff.address = address
        staff.gender = gender
        staff.mobile = mobile
        staff.status = status
        
        grade = Grade.objects.get(id = grade_id)
        staff.grade_id = grade      
        staff.save()
        messages.success(request,'Record is Successfully Updated !')
        return redirect('view_staff')
    return render(request,'Hod/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,'Record is Successfully Deleted !')
    return redirect('view_staff')

#=========================Staff Notification===================
@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff= Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff':staff,
        'see_notification':see_notification,
    }
    return render(request, 'Hod/staff_notification.html',context)

@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method=="POST":
        staff_id=request.POST.get('staff_id')
        message = request.POST.get('message')

        staff =Staff.objects.get (admin = staff_id) 
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )  
        notification.save()
        messages.success(request,'Notification Are Successfully Sent')
    return redirect('staff_send_notification')

def MGMT_SEND_NOTIFICATION(request):
    mgmt= Mgmt.objects.all()
    notification = Mgmt_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'mgmt':mgmt,
        'notification':notification,
    }
    return render(request, 'Hod/mgmt_notification.html', context)

def SAVE_MGMT_NOTIFICATION(request):
    if request.method=="POST":
        mgmt_id=request.POST.get('mgmt_id')
        message = request.POST.get('message')

        mgmt =Mgmt.objects.get (admin = mgmt_id) 
        stud_notification = Mgmt_Notification(
            mgmt_id = mgmt,
            message = message,
        )  
        stud_notification.save()
        messages.success(request,'Mgmt Notification is Successfully Sent.')
    return redirect('mgmt_send_notification')

#=======================Feedback=================================
def MGMT_FEEDBACK(request):
    feedback = Mgmt_Feedback.objects.all()
    feedback_history = Mgmt_Feedback.objects.all().order_by('-id')[0:5]
    context={
        'feedback':feedback,
        'feedback_history':feedback_history
    }
    return render(request,'Hod/mgmt_feedback.html',context)

def MGMT_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Mgmt_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
    return redirect('mgmt_feedback_reply')


def STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:5]
    context={
        'feedback':feedback,
        'feedback_history':feedback_history
    }
    return render(request,'Hod/staff_feedback.html',context)

def STAFF_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
    return redirect('staff_feedback_reply')

#===============Leave Section====================================

@login_required(login_url='/')
def MGMT_LEAVE_VIEW(request):
    mgmt_leave= Mgmt_leave.objects.all()

    context= {
        'mgmt_leave':mgmt_leave,
    }
    return render(request, 'Hod/mgmt_leave.html',context)

@login_required(login_url='/')
def MGMT_APPROVE_LEAVE(request,id):
    leave =Mgmt_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('mgmt_leave_view')

@login_required(login_url='/')
def MGMT_DISAPPROVE_LEAVE(request,id):
    leave =Mgmt_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('mgmt_leave_view')

@login_required(login_url='/')
def Staff_Leave_view(request):
    staff_leave= Staff_leave.objects.all()

    context= {
        'staff_leave':staff_leave,

    }
    return render(request, 'Hod/staff_leave.html',context)

@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request,id):
    leave =Staff_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_DISAPPROVE_LEAVE(request,id):
    leave =Staff_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')
def ADD_MONTH(request):
    if request.method == "POST":
        month_name = request.POST.get('month_name')
        month = Month(
            name = month_name,
        )
        month.save()
        messages.success(request,'Month is Successfully Created. ')
        
        return redirect('view_month')
    return render(request,'Hod/add_month.html')

@login_required(login_url='/')
def VIEW_MONTH(request):
    month = Month.objects.all()
    context = {
        'month':month,
    }
    return render(request,'Hod/view_month.html',context)

@login_required(login_url='/')
def EDIT_MONTH(request,id):
    month=Month.objects.get(id=id)
    context={
        'month':month,
    }
    return render(request,'Hod/edit_month.html',context)

@login_required(login_url='/')
def UPDATE_MONTH(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        month_id=request.POST.get('month_id')

        month=Month.objects.get(id=month_id)
        month.name=name
        month.save()
        messages.success(request,'Month is Successfully Updated.')
        return redirect('view_month')
    return render(request,'Hod/edit_month.html')

@login_required(login_url='/')
def DELETE_MONTH(request,id):
    month = Month.objects.get(id = id)
    month.delete()
    messages.success(request,'Month is Successfully Deleted')
    return redirect('view_month')

#===================Year==========================
@login_required(login_url='/')
def ADD_YEAR(request):
    if request.method == "POST":
        year_name = request.POST.get('year_name')
        year = Year(
            name = year_name,
        )
        year.save()
        messages.success(request,'Year is Successfully Created. ')
        
        return redirect('view_year')
    return render(request,'Hod/add_year.html')

@login_required(login_url='/')
def VIEW_YEAR(request):
    year = Year.objects.all()
    context = {
        'year':year,
    }
    return render(request,'Hod/view_year.html',context)

@login_required(login_url='/')
def EDIT_YEAR(request,id):
    year=Year.objects.get(id=id)
    context={
        'year':year,
    }
    return render(request,'Hod/edit_year.html',context)

@login_required(login_url='/')
def UPDATE_YEAR(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        year_id=request.POST.get('year_id')

        year=Year.objects.get(id=year_id)
        year.name=name
        year.save()
        messages.success(request,'Year is Successfully Updated.')
        return redirect('view_year')

    return render(request,'Hod/edit_year.html')

@login_required(login_url='/')
def DELETE_YEAR(request,id):
    year = Year.objects.get(id = id)
    year.delete()
    messages.success(request,'Year is Successfully Deleted')
    return redirect('view_year')

#+++++++++++++++++++++++++Payslip++++++++++++++++++++++++++++
def ADD_MGMT_SALARY(request):
    year = Year.objects.all()
    month = Month.objects.all()
    mgmt= Mgmt.objects.all()
    mgmt_salary = Mgmt_Salary.objects.all()
    if request.method == "POST":
        
        year_id = request.POST.get('year_id')
        month_id = request.POST.get('month_id')  
        mgmt_salary_id = request.POST.get('mgmt_salary_id')     
   
        year = Year.objects.get(id=year_id)
        month = Month.objects.get(id=month_id)

        mgmt_salary = Mgmt_Salary.objects.get(id=mgmt_salary_id)                      
 
    context = {
        'year':year, 
        'month':month, 
        'mgmt':mgmt, 
        'mgmt_salary':mgmt_salary,            
    }
    return render(request,'Hod/add_mgmt_salary.html',context)

def ADD_STAFF_SALARY(request):
    year = Year.objects.all()
    month = Month.objects.all()
    staff= Staff.objects.all()
    if request.method == "POST":
        
        year_id = request.POST.get('year_id')
        month_id = request.POST.get('month_id')       
   
        year = Year.objects.get(id=year_id)
        month = Month.objects.get(id=month_id)           
 
    context = {
        'year':year, 
        'month':month, 
        'staff':staff,             
    }
    return render(request,'Hod/add_staff_salary.html',context)

        
def VIEW_MGMT_SALARY(request):
    mgmt_salary = Mgmt_Salary.objects.all()
    context = {
        'mgmt_salary':mgmt_salary,
    }
    return render(request,'Hod/view_mgmt_salary.html',context)


 
#@login_required(login_url='/')
#def VIEW_PRODUCT(request):
    #product = Product.objects.all()
    #context = {
        #'product':product,
    #}
    #return render(request,'Hod/view_product.html',context)

