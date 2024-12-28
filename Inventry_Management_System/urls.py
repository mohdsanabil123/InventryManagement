from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from Inventry_Management_System.Inventry_Management_System import Hod_Views
from .import Hod_Views,views,Mgmt_Views,Staff_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),

    # Login Path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    # Profile Update
    path('profile/', views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),

    # This is Hod Panel url
    path('Hod/Home',Hod_Views.HOME,name='hod_home'),
    path('Hod/Mgmt/Add',Hod_Views.ADD_MGMT,name='add_mgmt'),
    path('Hod/Mgmt/View',Hod_Views.VIEW_MGMT,name='view_mgmt'),
    path('Hod/Mgmt/Edit/<str:id>',Hod_Views.EDIT_MGMT,name='edit_mgmt'),
    path('Hod/Mgmt/Update',Hod_Views.UPDATE_MGMT,name='update_mgmt'),
    path('Hod/Mgmt/Delete/<str:admin>',Hod_Views.DELETE_MGMT,name='delete_mgmt'),

    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),

    path('Hod/Add/Grade', Hod_Views.ADD_GRADE, name='add_grade'),
    path('Hod/view/Grade/', Hod_Views.VIEW_GRADE, name='view_grade'),
    path('Hod/Grade/Edit/<str:id>',Hod_Views.EDIT_GRADE,name='edit_grade'),
    path('Hod/Grade/Update',Hod_Views.UPDATE_GRADE,name='update_grade'),
    path('Hod/Grade/Delete/<str:id>',Hod_Views.DELETE_GRADE,name='delete_grade'),

    path('Hod/Mgmt/send_Notification',Hod_Views.MGMT_SEND_NOTIFICATION,name='mgmt_send_notification'),
    path('Hod/Mgmt/save_Notification',Hod_Views.SAVE_MGMT_NOTIFICATION,name='save_mgmt_notification'),
    
    path('Hod/Staff/send_Notification',Hod_Views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Hod/Staff/save_Notification',Hod_Views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('Hod/Mgmt/Feedback',Hod_Views.MGMT_FEEDBACK,name='mgmt_feedback_reply'),
    path('Hod/Mgmt/Feedback/save',Hod_Views.MGMT_FEEDBACK_SAVE,name='mgmt_feedback_reply_save'),

    path('Hod/Staff/Feedback',Hod_Views.STAFF_FEEDBACK,name='staff_feedback_reply'),
    path('Hod/Staff/Feedback/save',Hod_Views.STAFF_FEEDBACK_SAVE,name='reply_staff_feedback'),
    
    path('Hod/Mgmt/Leave_view',Hod_Views.MGMT_LEAVE_VIEW,name='mgmt_leave_view'),
    path('Hod/Mgmt/approve_leave/<str:id>',Hod_Views.MGMT_APPROVE_LEAVE,name='mgmt_approve_leave'),
    path('Hod/Mgmt/disapprove_leave/<str:id>',Hod_Views.MGMT_DISAPPROVE_LEAVE,name='mgmt_disapprove_leave'),
    
    path('Hod/Staff/Leave_view',Hod_Views.Staff_Leave_view,name='staff_leave_view'),
    path('Hod/Staff/approve_leave/<str:id>',Hod_Views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('Hod/Staff/disapprove_leave/<str:id>',Hod_Views.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),

    path('Hod/Month/Add',Hod_Views.ADD_MONTH,name='add_month'),
    path('Hod/Month/View',Hod_Views.VIEW_MONTH,name='view_month'),
    path('Hod/Month/Edit/<str:id>',Hod_Views.EDIT_MONTH,name='edit_month'),
    path('Hod/Month/Update',Hod_Views.UPDATE_MONTH,name='update_month'),
    path('Hod/Month/Delete/<str:id>',Hod_Views.DELETE_MONTH,name='delete_month'),

    path('Hod/Year/Add',Hod_Views.ADD_YEAR,name='add_year'),
    path('Hod/Year/View',Hod_Views.VIEW_YEAR,name='view_year'),
    path('Hod/Year/Edit/<str:id>',Hod_Views.EDIT_YEAR,name='edit_year'),
    path('Hod/Year/Update',Hod_Views.UPDATE_YEAR,name='update_year'),
    path('Hod/Year/Delete/<str:id>',Hod_Views.DELETE_YEAR,name='delete_year'),
    
    path('Hod/Mgmt/Salary/Add',Hod_Views.ADD_MGMT_SALARY,name='add_mgmt_salary'),
    path('Hod/Mgmt/Salary/View',Hod_Views.VIEW_MGMT_SALARY,name='view_mgmt_salary'),

    path('Hod/Staff/Salary/Add',Hod_Views.ADD_STAFF_SALARY,name='add_staff_salary'),
    
    
    

    # This is Mgmt url
    path('Mgmt/Home',Mgmt_Views.HOME,name='mgmt_home'),

    path('Mgmt/Notifications',Mgmt_Views.MGMT_NOTIFICATIONS,name='notification'),
    path('Mgmt/mark_as_done/<str:status>',Mgmt_Views.MGMT_NOTIFICATIONS_MARK_AS_DONE,name='mgmt_notification_mark_as_done'),

    #path('Mgmt/Notifications',Mgmt_Views.MGMT_NOTIFICATIONS,name='mgmt_notification'),
    #path('Mgmt/mark_as_done/<str:status>',Mgmt_Views.MGMT_NOTIFICATIONS_MARK_AS_DONE,name='mgmt_notification_mark_as_done'),

    path('Mgmt/Feedback',Mgmt_Views.MGMT_FEEDBACK,name='mgmt_feedback'),
    path('Mgmt/Feedback/save',Mgmt_Views.MGMT_FEEDBACK_SAVE,name='mgmt_feedback_save'),

    path('Mgmt/apply_for_leave',Mgmt_Views.MGMT_LEAVE,name='mgmt_leave'),
    path('Mgmt/Apply_leave_save',Mgmt_Views.MGMT_APPLY_LEAVE_SAVE,name='mgmt_apply_leave_save'),

    
    path('Mgmt/Product/Add',Mgmt_Views.ADD_PRODUCT,name='add_product'),
    path('Mgmt/Product/View',Mgmt_Views.VIEW_PRODUCT,name='view_product'),
    path('Mgmt/Product/Delete/<str:id>',Mgmt_Views.DELETE_PRODUCT,name='delete_product'),
    path('Mgmt/Product/Update',Mgmt_Views.UPDATE_PRODUCT,name='update_product'),
    path('Mgmt/Product/Edit/<str:id>',Mgmt_Views.EDIT_PRODUCT,name='edit_product'),
    
    path('Mgmt/Supplier/Add',Mgmt_Views.ADD_SUPPLIER,name='add_supplier'),
    path('Mgmt/Supplier/View',Mgmt_Views.VIEW_SUPPLIER,name='view_supplier'),
    path('Mgmt/Supplier/Edit/<str:id>',Mgmt_Views.EDIT_SUPPLIER,name='edit_supplier'),
    path('Mgmt/Supplier/Update',Mgmt_Views.UPDATE_SUPPLIER,name='update_supplier'),
    path('Mgmt/Supplier/Delete/<str:id>',Mgmt_Views.DELETE_SUPPLIER,name='delete_supplier'),

    path('Mgmt/Add/Purchase', Mgmt_Views.ADD_PURCHASE, name='add_purchase'),
    path('Mgmt/view/Purchase/', Mgmt_Views.VIEW_PURCHASE, name='view_purchase'),
    path('Mgmt/Purchase/Edit/<str:id>',Mgmt_Views.EDIT_PURCHASE,name='edit_purchase'),
    path('Mgmt/Purchase/Update',Mgmt_Views.UPDATE_PURCHASE,name='update_purchase'),
    path('Mgmt/Purchase/Delete/<str:id>',Mgmt_Views.DELETE_PURCHASE,name='delete_purchase'),
    


    # This is Staff url
    path('Staff/Home',Staff_Views.HOME,name='staff_home'),

    #path('Staff/Notifications',Staff_Views.NOTIFICATIONS,name='notifications'),
    #path('Staff/mark_as_done/<str:status>',Staff_Views.STAFF_NOTIFICATIONS_MARK_AS_DONE,name='staff_notification_mark_as_done'),
    
    path('Staff/Notifications',Staff_Views.STAFF_NOTIFICATIONS,name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_Views.STAFF_NOTIFICATIONS_MARK_AS_DONE,name='staff_notification_mark_as_done'),
    
    #path('Staff/Apply_leave',Staff_Views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    #path('Staff/Apply_leave_save',Staff_Views.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),

    path('Staff/Feedback',Staff_Views.STAFF_FEEDBACK,name='staff_feedback'),
    path('Staff/Feedback/save',Staff_Views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),

    path('Staff/Apply_leave',Staff_Views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Staff/Apply_leave_save',Staff_Views.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
