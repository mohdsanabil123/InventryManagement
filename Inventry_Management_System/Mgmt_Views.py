from django.shortcuts import render,redirect
from app.models import Mgmt, Mgmt_Notification, Mgmt_leave, Mgmt_Feedback, Product,Supplier,Purchase
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def HOME(request):
    return render(request, 'Mgmt/home.html')

@login_required(login_url='/')
def MGMT_NOTIFICATIONS(request):
    mgmt= Mgmt.objects.filter(admin=request.user.id)
    for i in mgmt:
        mgmt_id=i.id
        notification=Mgmt_Notification.objects.filter(mgmt_id=mgmt_id)

        context={
            'notification':notification,
        }
    
        return render(request, 'Mgmt/notification.html',context)
    
@login_required(login_url='/')
def MGMT_NOTIFICATIONS_MARK_AS_DONE(request, status):
    notification = Mgmt_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


def MGMT_FEEDBACK(request):
    mgmt_id=Mgmt.objects.get(admin=request.user.id)
    feedback_history= Mgmt_Feedback.objects.filter(mgmt_id=mgmt_id)

    context= {
        'feedback_history':feedback_history,
    }
    return render(request, 'Mgmt/feedback.html',context)

def MGMT_FEEDBACK_SAVE(request):
    if request.method=='POST':
        feedback=request.POST.get('feedback')
        mgmt=Mgmt.objects.get(admin=request.user.id)

        feedback=Mgmt_Feedback(
            mgmt_id=mgmt,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()
        return redirect('mgmt_feedback')
    
def MGMT_LEAVE(request):
    mgmt=Mgmt.objects.filter(admin=request.user.id)
    for i in mgmt:
        mgmt_id = i.id

        mgmt_leave_history = Mgmt_leave.objects.filter(mgmt_id=mgmt_id)
        context={
            'mgmt_leave_history':mgmt_leave_history,
        }
    return render(request,'Mgmt/apply_leave.html', context)
    
@login_required(login_url='/')
def MGMT_APPLY_LEAVE_SAVE(request):
    if request.method=='POST':
        leave_date=request.POST.get('leave_date')
        leave_message=request.POST.get('leave_message')

        mgmt=Mgmt.objects.get(admin=request.user.id)

        leave=Mgmt_leave(
            mgmt_id=mgmt,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request,'Leave Applied Successfully.')
    return redirect('mgmt_leave')



#=========================Product=========================
@login_required(login_url='/')
def ADD_PRODUCT(request):    
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_unit = request.POST.get('product_unit')
        product_status = request.POST.get('product_status')
        product_category = request.POST.get('product_category') 
        
        product = Product(
            name = product_name,
            unit = product_unit,
            status = product_status,
            category = product_category,
        )
        product.save()
        messages.success(request,'Product is Successfully Created. ')       
        return redirect('view_product')
    
    return render(request,'Mgmt/add_product.html')

@login_required(login_url='/')
def VIEW_PRODUCT(request):
    product = Product.objects.all()   
    context = {
        'product':product,       
    }
    return render(request,'Mgmt/view_product.html',context)

@login_required(login_url='/')
def EDIT_PRODUCT(request,id):
    product=Product.objects.get(id=id)
    
    context={
        'product':product,       
    }
    return render(request,'Mgmt/edit_product.html',context)

@login_required(login_url='/')
def UPDATE_PRODUCT(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        unit=request.POST.get('unit')
        status=request.POST.get('status')
        category=request.POST.get('category')
        product_id=request.POST.get('product_id')
        product=Product.objects.get(id=product_id)
        
        product.name=name
        product.unit=unit
        product.status=status
        product.category=category
        product.save()
         
        messages.success(request,'Product is Successfully Updated.')
        return redirect('view_product')
    return render(request,'Mgmt/edit_product.html') 

@login_required(login_url='/')
def DELETE_PRODUCT(request, id):    
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('view_product')

#==================Supplier=========================
@login_required(login_url='/')
def ADD_SUPPLIER(request):
    if request.method == "POST":
        supplier_name = request.POST.get('supplier_name')        
        supplier_company = request.POST.get('supplier_company')
        supplier_address = request.POST.get('supplier_address') 
        supplier_mobile = request.POST.get('supplier_mobile') 
        supplier_email = request.POST.get('supplier_email') 
        supplier_status = request.POST.get('supplier_status') 

        supplier = Supplier(
            name = supplier_name,           
            company = supplier_company,
            address = supplier_address,           
            mobile = supplier_mobile,
            email = supplier_email,           
            status = supplier_status,
        )
        supplier.save()
        messages.success(request,'Supplier is Successfully Created. ')        
        return redirect('view_supplier')
    return render(request,'Mgmt/add_supplier.html')

@login_required(login_url='/')
def VIEW_SUPPLIER(request):
    supplier = Supplier.objects.all()   
    context = {
        'supplier':supplier,       
    }
    return render(request,'Mgmt/view_supplier.html',context)

@login_required(login_url='/')
def EDIT_SUPPLIER(request,id):
    supplier=Supplier.objects.get(id=id)
    context={
        'supplier':supplier,
    }
    return render(request,'Mgmt/edit_supplier.html',context)

@login_required(login_url='/')
def UPDATE_SUPPLIER(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        company=request.POST.get('company') 
        mobile=request.POST.get('mobile') 
        email=request.POST.get('email')  
        address=request.POST.get('address')       
        status=request.POST.get('status')
        supplier_id=request.POST.get('supplier_id')
        supplier=Supplier.objects.get(id=supplier_id)
        supplier.name=name 
        supplier.company=company
        supplier.mobile=mobile
        supplier.email=email
        supplier.address=address
        supplier.status=status
        supplier.save()
        messages.success(request,'Supplier is Successfully Updated.')
        return redirect('view_supplier')
    return render(request,'Mgmt/edit_supplier.html')

@login_required(login_url='/')
def DELETE_SUPPLIER(request, id):    
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    return redirect('view_supplier')

#===============================Purchase=====================
@login_required(login_url='/')
def ADD_PURCHASE(request):
    product = Product.objects.all()
    supplier = Supplier.objects.all()    
    if request.method == "POST":
        purc_price = request.POST.get('purc_price')
        purc_quantity = request.POST.get('purc_quantity')
        purc_cost = request.POST.get('purc_cost')
        sale_price = request.POST.get('sale_price')
        lot_no = request.POST.get('lot_no')
        mrp = request.POST.get('mrp')
        exp_date = request.POST.get('exp_date')
        total_cost = request.POST.get('total_cost')
                     
        product_id = request.POST.get('product_id') 
        product = Product.objects.get(id=product_id)

        supplier_id = request.POST.get('supplier_id') 
        supplier = Supplier.objects.get(id=supplier_id)
            
        purchase = Purchase(
            purc_price = purc_price,
            purc_quantity = purc_quantity,
            purc_cost = purc_cost,
            sale_price = sale_price,
            lot_no = lot_no,
            mrp = mrp,
            exp_date =exp_date,
            total_cost =total_cost,
            product_id = product,
            supplier_id = supplier,          
        )
        purchase.save()
        messages.success(request,'Purchase is Successfully Created. ')       
        return redirect('view_purchase')
    context = {
        'product':product,
        'supplier':supplier,                     
    }
    return render(request,'Mgmt/add_purchase.html',context)

@login_required(login_url='/')
def VIEW_PURCHASE(request):
    purchase=Purchase.objects.all()
    context={
        'purchase':purchase,
    }
    return render (request, 'Mgmt/view_purchase.html',context)

@login_required(login_url='/')
def EDIT_PURCHASE(request,id):
    purchase=Purchase.objects.filter(id=id)
    product=Product.objects.all()
    supplier=Supplier.objects.all()  
    context={
        'purchase':purchase,
        'product':product,
        'supplier':supplier,             
    }
    return render(request,'Mgmt/edit_purchase.html',context)

@login_required(login_url='/')
def UPDATE_PURCHASE(request):
    if request.method== 'POST':
        purc_price=request.POST.get('purc_price')
        purc_quantity=request.POST.get('purc_quantity') 
        purc_cost=request.POST.get('purc_cost') 
        sale_price=request.POST.get('sale_price')  
        lot_no=request.POST.get('lot_no')       
        mrp=request.POST.get('mrp')
        pur_date=request.POST.get('pur_date')
        exp_date=request.POST.get('exp_date')
        purchase_id=request.POST.get('purchase_id')     
        product_id = request.POST.get('product_id')
        supplier_id = request.POST.get('supplier_id')

        purchase=Purchase.objects.get(id=purchase_id) 
        purchase.purc_price = purc_price
        purchase.purc_quantity = purc_quantity
        purchase.purc_cost =purc_cost
        purchase.sale_price = sale_price
        purchase.lot_no = lot_no
        purchase.mrp = mrp
        purchase.exp_date = exp_date
        purchase.pur_date = pur_date
        product = Product.objects.get(id = product_id)
        purchase.product_id = product 
        purchase.save()
        supplier = Supplier.objects.get(id = supplier_id)
        purchase.supplier_id = supplier 
        purchase.save()
        print(purchase_id)
        messages.success(request,'Purchase record is Successfully Updated !')
        return redirect('view_purchase')
    return render(request,'Mgmt/edit_purchase.html')


@login_required(login_url='/')
def DELETE_PURCHASE(request, id):
    purchase = Purchase.objects.get(id=id)
    purchase.delete()
    return redirect('view_purchase')