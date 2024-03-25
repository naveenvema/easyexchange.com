from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.



def Home(request):
    allproducts=Sellerproducts.objects.filter(status='Confirm')
    print(allproducts)
    customers=Customers.objects.all()
    happy_customers=customers.count()
    products=Sellerproducts.objects.all()
    totalproducts=products.count()
    context={'allproducts':allproducts,'happy_customers':happy_customers,'totalproducts':totalproducts}
    return render(request,'main-home.html',context)



def admin_dashboard(request):
    customer=Customers.objects.all()
    product=Sellerproducts.objects.all()
    customers=customer.count()
    
    products=product.count()

    alerts=Send_Details.objects.all()
    print(alerts)
    notifications=alerts.count()
   
    context={'customers':customers,'products':products,'notifications':notifications}
    return render(request,'adminpage2.html',context)


def admin_manage_products(request):
    products=Sellerproducts.objects.filter().order_by('-created_at')
    Allproducts=products.count()
    if request.method=='POST':
        status=request.POST['dropdown']
        print(status)
        order_id=request.POST['order_id']
        print(order_id)
        order_to_update = Sellerproducts.objects.get(id=order_id)
        order_to_update.status=status
        order_to_update.save()
    context={'products':products,'Allproducts':Allproducts}
    return render(request,'admin_product_page.html',context)





def admin_singleproduct(request,id):

    single=Sellerproducts.objects.get(id=id)
    print(single)

    context={'single':single}
    return render(request,'admin_single_product2.html',context)





def admin_manage_customers(request):
    customer=Customers.objects.all()
    
    customers=customer.count()
    context={'customers':customers,'customer':customer}
    return render(request,'admin_customers_page.html',context)



def happy_customers(request):
    customers=Happy_Customers.objects.all()
    noofcustomers=customers.count()


    context={'customers':customers,'noofcustomers':noofcustomers}
    return render(request,'happy_customers_page.html',context)


def unstisfied_customers(request):
    customers=Unsatisfied_Customers.objects.all()
    noofproducts=customers.count()
    context={'customers':customers,'noofproducts':noofproducts}
    return render(request,'unsatisfied_customers.html',context)




def admin_edit(request):
    return render(request,'adminedit.html')



def admin_update(request, id):
    user_to_update = get_object_or_404(User, id=id)
    print(user_to_update)
    

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if a new profile picture is being uploaded
        # Update the desired fields
        user_to_update.username = username
        user_to_update.email = email
        user_to_update.password = password

        # Save the changes to the database
        user_to_update.save()
        

    # Print the image URL for debugging
        return redirect("admin_dashboard")
    else:
        # If the request method is not POST, return a bad request response
        return HttpResponseBadRequest("Invalid request method")



def Register(request):
    form=CreateUserForm()

    if request.method=='POST':
        city=request.POST['city']
        phone_number=request.POST['phone_number']
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            username=form.cleaned_data.get('username')
            Customers.objects.create(user=user,name=user.username,email=user.email,city=city,phone_number=phone_number)
            print("user created successfilly")
            #messages.success(request,user+username)
            return redirect('/')
    context={'form':form} 
    return render(request,'register.html',context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        #username = request.POST.get("username", False)
        #password = request.POST.get("password", False)
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')

            login(request, user)
            #return render(request,'fashion3.html')
            return redirect("splitpage")
        else:
            messages.warning(request, 'Invalid Username/password')
            return redirect("login_user")
    
    return render(request,'login.html')


def splitpage(request):
    return render(request,'splitpage.html')

def seller_page(request):
    user = request.user
    #print(user)
    seller = user.customers
    sellerproducts = Sellerproducts.objects.filter(customer=seller)
    noofproducts=sellerproducts.count()
    #print(sellerproducts)
    notifications = Notification.objects.filter(seller_product__customer=seller).order_by('-timestamp')
    noofnotification=notifications.count()
    #print(noofnotification)
    #print(notifications)
    intrest=Intrested.objects.filter(seller_product__customer=seller)
    noofintrest=intrest.count()

    context={'sellerproducts':sellerproducts,'noofproducts':noofproducts,'noofnotification':noofnotification,'noofintrest':noofintrest}

    return render(request,'sellerpage3.html',context)

def delete_sellerproducts(request,id):
    deleteitem=Sellerproducts.objects.get(id=id)
    seller_name=deleteitem.customer
    product_name=deleteitem.Product_Name
    product_image=deleteitem.product_image1
    product_price=deleteitem.price
    product_city=deleteitem.customer.city
    upload_date=deleteitem.created_at
    category=deleteitem.Category
    Unsatisfied_Customers.objects.create(seller_name=seller_name,product_name=product_name,product_image=product_image,category=category,product_price=product_price,product_city=product_city,upload_date=upload_date)
    print(deleteitem)
    deleteitem.delete()
    return redirect('seller_page')



def selling_successfullly(request,id):
    selling_items=Sellerproducts.objects.get(id=id)
    seller_name=selling_items.customer
    product_name=selling_items.Product_Name
    product_image=selling_items.product_image1
    product_price=selling_items.price
    product_city=selling_items.customer.city
    upload_date=selling_items.created_at
    category=selling_items.Category 
    print(product_name,seller_name,product_price,product_city,upload_date,category,product_image)
    Happy_Customers.objects.create(seller_name=seller_name,product_name=product_name,product_image=product_image,category=category,product_price=product_price,product_city=product_city,upload_date=upload_date)
    print("created succesfully")

    selling_items.delete()
    return redirect('seller_page')




def clothing(request):
    user=request.user
    #print(user)
    buyerproducts=Sellerproducts.objects.filter(status='Confirm',Category=1)
    #for i in buyerproducts:
        #print(i,i.price)
    buyer = user.customers
    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)
    notifications=alerts.count()
    context={'buyerproducts':buyerproducts,'notifications':notifications}
    return render(request,'clothing.html',context)
    



def eletronic_gadgets(request):
    user=request.user
    #print(user)
    buyerproducts=Sellerproducts.objects.filter(status='Confirm',Category=2)
    #for i in buyerproducts:
        #print(i,i.price)
    buyer = user.customers
    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)
    notifications=alerts.count()

    context={'buyerproducts':buyerproducts,'notifications':notifications}
    return render(request,'electronicgadgets.html',context)




def homely_furniture(request):
    user=request.user
    #print(user)
    buyerproducts=Sellerproducts.objects.filter(status='Confirm',Category=3)
    #for i in buyerproducts:
        #print(i,i.price)
    
    buyer = user.customers
    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)
    notifications=alerts.count()
    
    context={'buyerproducts':buyerproducts,'notifications':notifications}
    return render(request,'homelyfurniture.html',context)


def vehicles(request):
    user=request.user
    #print(user)
    buyerproducts=Sellerproducts.objects.filter(status='Confirm',Category=4)
    #for i in buyerproducts:
        #print(i,i.price)
    buyer = user.customers
    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)
    notifications=alerts.count()
    context={'buyerproducts':buyerproducts,'notifications':notifications}
    return render(request,'vehicles.html',context)

def others(request):
    user=request.user
    #print(user)
    buyerproducts=Sellerproducts.objects.filter(status='Confirm',Category=5)
    #for i in buyerproducts:
        #print(i,i.price)
    buyer = user.customers
    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)
    notifications=alerts.count()
    context={'buyerproducts':buyerproducts,'notifications':notifications}
    return render(request,'others.html',context)

def buyer_page(request):
    user=request.user
    buyer = user.customers

    buyerproducts=Sellerproducts.objects.filter(status='Confirm')

    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)
    notifications=alerts.count()


    context={'buyerproducts':buyerproducts,'notifications':notifications}
    return render(request,'buyerpage.html',context)

def buyer_alerts(request):

    user=request.user
    buyer=user.customers
    senddetails=Send_Details.objects.filter(buyer=buyer)
    responses=senddetails.count()
    context={'senddetails':senddetails,'responses':responses}
    return render(request,'buyeralerts.html',context)


def like_product(request,id):
    buyer=request.user.customers
    product = get_object_or_404(Sellerproducts, id=id)
    seller = product.customer
    message = f" Hey '{seller}' Your product '{product.Product_Name}' has been liked by {buyer.name}."
    #print(message)
    notification=Notification.objects.all()
    #print(notification)
    notify=[]
    for i in notification:
        notify.append(i.message)
    if message in notify:
        print("already liked")
        messages.warning(request, 'already liked')
        return redirect("go_to_details",id=id)
    else:
        Notification.objects.create(buyer=buyer,seller_product=product, message=message)
        print(Notification)
    
    return redirect('go_to_details', id=id)


def intrested(request,id):
    buyer=request.user.customers
    product = get_object_or_404(Sellerproducts, id=id)
    seller = product.customer
    print(buyer,product,seller)

    intrest=f"Hey '{seller}',I am '{buyer.name}',i  intrested to buy your '{product}' plz send details"

    intrests=Intrested.objects.all()
    intresttobuy=[]
    for i in intrests:
        intresttobuy.append(i.message)
    
    if intrest in intresttobuy:
        print("already you intrested")
    else:
        Intrested.objects.create(buyer=buyer,seller_product=product,message=intrest)

    print(intrest)
    return redirect('go_to_details', id=id)




def go_to_details(request,id):
    details=Sellerproducts.objects.get(id=id)
    print(details)
    like=Notification.objects.filter(seller_product=details)
    likes=like.count()
    details=Sellerproducts.objects.get(id=id)
    print(details)
    #print(details,details.price,details.name,details.id)
    like=Notification.objects.filter(seller_product=details)
    likes=like.count()
    intrest=Intrested.objects.filter(seller_product=details)
    intrests=intrest.count()
    user=request.user
    buyer = user.customers
    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)
    notifications=alerts.count()
    context={'details':details,'likes':likes,'intrests':intrests,'notifications':notifications}
    return render(request,'singleproduct.html',context)

def add_your_product(request):
    if request.method == 'POST':
        form=ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            user=request.user
            customer=Customers.objects.get(name=user)
            print(customer)
            sellerproducts = Sellerproducts(customer=customer)
            #sellerproducts.save()
            # Set the instance of the form to the created sellerproducts instance
            form.instance.customer = customer
            form.instance.status = 'Pending'
             # Set the status if needed
            form.instance.save()
            return redirect('seller_page')
    else:
        form=ProductsForm()
    context={'form':form}
    return render(request,'add_your_product.html',context)



def alerts(request):
    user = request.user
    print(user)
    seller = user.customers
    print(seller)
    notifications = Notification.objects.filter(seller_product__customer=seller).order_by('-timestamp')
    nooflikes=notifications.count()
    print(nooflikes)
    sellerproducts = Sellerproducts.objects.filter(customer=seller)
    noofproducts=sellerproducts.count()
    context = {'customer': seller, 'notifications': notifications,'noofproducts':noofproducts,'nooflikes':nooflikes}
    print(notifications)
    return render(request,'likes.html',context)



def intrested_buyers(request):

    user = request.user
    #print(user)
    seller = user.customers
    #print(seller)
    intrestedbuyers = Intrested.objects.filter(seller_product__customer=seller).order_by('-time')
    notifications = Notification.objects.filter(seller_product__customer=seller).order_by('-timestamp')
    nooflikes=notifications.count()
    intrest=Intrested.objects.filter(seller_product__customer=seller)
    noofintrest=intrest.count()

    sellerproducts = Sellerproducts.objects.filter(customer=seller)
    noofproducts=sellerproducts.count()


    context = {'intrestedbuyers':intrestedbuyers,'customer': seller, 'notifications': notifications,'nooflikes':nooflikes,'noofintrest':noofintrest,'noofproducts':noofproducts}

    #print(intrestedbuyers)

   
    return render(request,'intrestedbuyers.html',context)


def send_details(request,id):
    message=Intrested.objects.get(id=id)
    print(message)
    buyer=message.buyer
    print(buyer)
    product=message.seller_product
    print(product)
    user = request.user
    print(user)
    seller = user.customers
    seller_ph=Customers.objects.get(name=seller)
    print(seller_ph.phone_number)
    message=f" Hi {buyer},I am {seller} Thanks for your interest in {product} . I'm the seller. Feel free to reach me at {seller_ph.phone_number} for any questions or to make a purchase."
    print(message)

    notification=Send_Details.objects.all()
    #print(notification)
    notify=[]
    for i in notification:
        notify.append(i.message)
    if message in notify:
        print("already send it")
    else:
        Send_Details.objects.create(buyer=buyer,seller_product=product,message=message)

    alerts=Send_Details.objects.filter(buyer=buyer)
    print(alerts)

    return redirect('intrested_buyers')



def edit(request):
    return render(request,'edit2.html')


"""def update(request, id):
    user_to_update = get_object_or_404(User, id=id)
    customer_to_update = get_object_or_404(Customers, user=user_to_update)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        phone_number=request.POST['phone_number']
        # Check if a new profile picture is being uploaded
        # Update the desired fields
        user_to_update.username = username
        user_to_update.email = email
        user_to_update.password = password



        customer_to_update = get_object_or_404(Customers, user=user_to_update)
        customer_to_update.city = city
        customer_to_update.phone_number = phone_number
        customer_to_update.save()
        

        # Save the changes to the database
        user_to_update.save()
        customer_to_update.save()
    return redirect("splitpage")"""
from django.http import HttpResponseBadRequest

def update(request, id):
    user_to_update = get_object_or_404(User, id=id)
    customer_to_update = get_object_or_404(Customers, user=user_to_update)

    if request.method == 'POST':
        # Get values from request.POST with default values as empty strings
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        city = request.POST.get('city', '')
        phone_number = request.POST.get('phone_number', '')

        # Update the desired fields
        user_to_update.username = username
        user_to_update.email = email
        user_to_update.password = password

        customer_to_update.city = city
        customer_to_update.phone_number = phone_number
        customer_to_update.save()

        # Save the changes to the database
        user_to_update.save()
        customer_to_update.save()
        return redirect("splitpage")
    else:
        # If the request method is not POST, return a bad request response
        return HttpResponseBadRequest("Invalid request method")




"""def update(request, id):
    user_to_update = get_object_or_404(User, id=id)
    form = CreateUserForm(request.POST or None, instance=user_to_update)

    if request.method == 'POST' and form.is_valid():
        # Update the desired fields
        user_to_update.username = form.cleaned_data['username']
        user_to_update.email = form.cleaned_data['email']
        user_to_update.save()

        # Update the related customer instance
        customer_to_update = get_object_or_404(Customers, user=user_to_update)
        customer_to_update.city = form.cleaned_data['city']
        customer_to_update.phone_number = form.cleaned_data['phone_number']
        customer_to_update.save()

        return redirect("splitpage")

    return render(request, 'edit2.html', {'form': form, 'user': user_to_update})
"""





def logout_user(request):
    logout(request)
    return redirect('/')





