from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='customers')
    """user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)"""
    name=models.CharField(max_length=150,null=True)
    email=models.EmailField(max_length=150,null=True)
    city=models.CharField(max_length=150,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    profile_pic=models.ImageField(upload_to="uploads",default='profile.jpg',null=True)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
class Sellerproducts(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Confirm','Confirm')
    )
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Product_Name=models.CharField(max_length=150)
    Category=models.ForeignKey(Category,default=1,null=True,on_delete=models.SET_NULL)
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(null=True)
    description=models.CharField(max_length=300,default="",null=True)
    status=models.CharField(max_length=70,choices=STATUS,null=True)  
    product_image1=models.ImageField(upload_to="uploads",)
    product_image2=models.ImageField(upload_to="uploads",null=True)
    product_image3=models.ImageField(upload_to="uploads",null=True)
    product_image4=models.ImageField(upload_to="uploads",null=True)
    product_image5=models.ImageField(upload_to="uploads",null=True)
    def __str__(self):
        return self.Product_Name
    

class Notification(models.Model):
    buyer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    seller_product = models.ForeignKey(Sellerproducts, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    


class Intrested(models.Model):
    buyer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    seller_product = models.ForeignKey(Sellerproducts, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    
    
class Send_Details(models.Model):
    buyer=models.ForeignKey(Customers, on_delete=models.CASCADE)
    seller_product = models.ForeignKey(Sellerproducts, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    


class Happy_Customers(models.Model):
    seller_name=models.CharField(max_length=150)
    product_name=models.CharField(max_length=150)
    product_image=models.ImageField(upload_to="happy_customers")
    product_price=models.IntegerField(null=True)
    category=models.CharField(max_length=150)
    product_city=models.CharField(max_length=150)
    upload_date=models.DateTimeField()
    selling_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name
    

class Unsatisfied_Customers(models.Model):
    seller_name=models.CharField(max_length=150)
    product_name=models.CharField(max_length=150)
    product_image=models.ImageField(upload_to="happy_customers")
    product_price=models.IntegerField(null=True)
    category=models.CharField(max_length=150)
    product_city=models.CharField(max_length=150)
    upload_date=models.DateTimeField()
    delete_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name

    

