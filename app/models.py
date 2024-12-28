from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER=(
        ('1','HOD'),
        ('2','MGMT'),
        ('3','STAFF'),
    )
    user_type=models.CharField(choices=USER,max_length=50,default=1)
    profile_pic=models.ImageField(upload_to='media/profile_pic')

#============ Grade Model=============================
class Grade(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
#=================== Month Model ===========================
class Month(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

#============== Year Model =====================
class Year(models.Model):
    name = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
#============ Management Model=============================
class Mgmt(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    grade_id = models.ForeignKey(Grade,on_delete=models.DO_NOTHING)
    mobile=models.IntegerField(null=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
        
 #============ Staff Model=============================   
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100) 
    grade_id = models.ForeignKey(Grade,on_delete=models.DO_NOTHING)
    mobile=models.IntegerField(null=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
    
class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.staff_id.admin.first_name + " "  + self.staff_id.admin.last_name
    
class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
class Mgmt_leave(models.Model):
    mgmt_id = models.ForeignKey(Mgmt,on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.mgmt_id.admin.first_name + " " + self.mgmt_id.admin.last_name

class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
class Mgmt_Feedback(models.Model):
    mgmt_id = models.ForeignKey(Mgmt,on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.mgmt_id.admin.first_name + " " + self.mgmt_id.admin.last_name
    
class Mgmt_Notification(models.Model):
    mgmt_id = models.ForeignKey(Mgmt,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.mgmt_id.admin.first_name + " "  + self.mgmt_id.admin.last_name


#============ Product Model=============================
class Product(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    mobile=models.IntegerField(null=True)
    email=models.EmailField(max_length=50)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
#==================Purchase============================
# Model for Purchase Transaction
class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)   
    purc_price = models.DecimalField(max_digits=10, decimal_places=2)
    purc_quantity = models.PositiveIntegerField()
    purc_cost = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    lot_no = models.CharField(max_length=255)
    mrp = models.IntegerField(default=0)
    pur_date = models.DateField(auto_now_add=True)
    exp_date = models.DateField()
    updated_at = models.DateField(auto_now=True) 
    total_cost = models.DecimalField(max_digits=15, decimal_places=2, editable=False)

    #def save(self, *args, **kwargs):
        # Calculate total_cost
        #self.total_cost = self.purc_cost * self.purc_quantity
        #super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase of {self.product.name} by {self.supplier.name} on {self.expiry_date}"



