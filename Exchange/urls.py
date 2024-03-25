"""
URL configuration for Exchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from EasyExchange import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="HOME"),
    path("Register",views.Register,name="Register"),
    path("login_user",views.login_user,name="login_user"),
    path("splitpage",views.splitpage,name="splitpage"),

    path("seller_page",views.seller_page,name="seller_page"),
    path("buyer_page",views.buyer_page,name="buyer_page"),
    path("logout_user",views.logout_user,name="logout_user"),
    path("add_your_product",views.add_your_product,name="add_your_product"),
    path("delete_sellerproducts/<int:id>",views.delete_sellerproducts,name="delete_sellerproducts"),
    path("go_to_details/<int:id>",views.go_to_details,name="go_to_details"),
    path("edit",views.edit,name="edit"),
    path("update/<int:id>",views.update,name="update"),
    path("buyer_alerts",views.buyer_alerts,name="buyer_alerts"),
    path("like_product/<int:id>",views.like_product,name="like_product"),
    path("intrested/<int:id>",views.intrested,name="intrested"),
    path("alerts",views.alerts,name="alerts"),
    path("intrested_buyers",views.intrested_buyers,name="intrested_buyers"),
    path("send_details/<int:id>",views.send_details,name="send_details"),
    path("admin_dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("admin_manage_products",views.admin_manage_products,name="admin_manage_products"),
    path("admin_manage_customers",views.admin_manage_customers,name="admin_manage_customers"),
    path("admin_edit",views.admin_edit,name="admin_edit"),
    path("admin_update/<int:id>",views.admin_update,name="admin_update"),
    path("selling_successfullly/<int:id>",views.selling_successfullly,name="selling_successfullly"),
    path("happy_customers",views.happy_customers,name="happy_customers"),
    path("unstisfied_customers",views.unstisfied_customers,name="unstisfied_customers"),
    path("admin_singleproduct/<int:id>",views.admin_singleproduct,name="admin_singleproduct"),
    path("clothing",views.clothing,name="clothing"),
    path("eletronic_gadgets",views.eletronic_gadgets,name="eletronic_gadgets"),
    
    path("homely_furniture",views.homely_furniture,name="homely_furniture"),
    path("vehicles",views.vehicles,name="vehicles"),
    path("others",views.others,name="others"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),
    #path("admin_edit",views.admin_edit,name="admin_edit"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
