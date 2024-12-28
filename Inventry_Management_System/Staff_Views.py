from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Staff_Notification, Staff , Staff_Feedback , Staff_leave
@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')

def STAFF_NOTIFICATIONS(request):
    staff= Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id=i.id
        notification=Staff_Notification.objects.filter(staff_id=staff_id)

        context={
            'notification':notification,
        }
    
        return render(request, 'Staff/notification.html',context)
    
@login_required(login_url='/')
def STAFF_NOTIFICATIONS_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

def STAFF_FEEDBACK(request):
    staff_id=Staff.objects.get(admin=request.user.id)
    feedback_history= Staff_Feedback.objects.filter(staff_id=staff_id)

    context= {
        'feedback_history':feedback_history,
    }
    return render(request, 'Staff/feedback.html',context)

def STAFF_FEEDBACK_SAVE(request):
    if request.method=='POST':
        feedback=request.POST.get('feedback')
        staff=Staff.objects.get(admin=request.user.id)

        feedback=Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()
        return redirect('staff_feedback')
    
@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id=staff_id)
        context={
            'staff_leave_history':staff_leave_history,
        }
    return render(request,'Staff/apply_leave.html', context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method=='POST':
        leave_date=request.POST.get('leave_date')
        leave_message=request.POST.get('leave_message')

        staff=Staff.objects.get(admin=request.user.id)

        leave=Staff_leave(
            staff_id=staff,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request,'Leave Applied Successfully.')
    return redirect('staff_apply_leave')

