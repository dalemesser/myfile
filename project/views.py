from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from .forms import OrderForm,CustomerForm,RegisterForm
from django.http import HttpResponseRedirect,HttpResponse
from django.forms import inlineformset_factory
from .filters import OrderFilter,ProductFilter
from django.contrib import messages
from django.contrib.auth import authenticate,logout, login as dj_login
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_user,admin_only
from django.contrib.auth.models import Group


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request,"Accounted was Created Succussfully of" + username)
                return redirect(reverse('login'))
        contex = {
        "form":form
        }
        return render(request,"project/register.html",contex)
@unauthenticated_user
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get("password")
        user =authenticate(request,username=username , password= password)

        if user is not None:
            dj_login(request, user)
            return redirect(reverse('home'))
        else:
            messages.info(request,"Username  of Password incorect")
            return redirect(reverse("login"))

    contex={

    }
    return render(request,"project/login.html",contex)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
#@allowed_user(allowed_roles=["admin"])
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    totol_customers = customers.count()
    totol_orders = orders.count()
    dilivered = orders.filter(status="Dilivered").count()
    pending = orders.filter(status = "Pending").count()
    context ={
        "orders":orders,
        "customers" : customers,
        "totol_customers":totol_customers,
        "totol_orders" : totol_orders,
        "dilivered" : dilivered ,
        "pending" : pending
    }
    return render(request,"project/dashboard.html",context)

@login_required(login_url="login")
@admin_only
def products(request):
    products=Product.objects.all()
    myFilter = ProductFilter(request.GET,queryset=products)
    products = myFilter.qs
    context = {
        "products":products,
        "myFilter":myFilter
    }
    return render(request,"project/products.html",context)



def customer(request,id):
    customer = Customer.objects.get(id=id)
    orders_total = customer.order_set.all().count()
    orders = customer.order_set.all()
    myFilter = OrderFilter(request.GET , queryset=orders)
    orders = myFilter.qs

    context = {
        "customer":customer,
        "orders_total":orders_total,
        "orders":orders,
        "myFilter":myFilter
    }
    return render(request,"project/customer.html",context)
@login_required(login_url="login")
@admin_only
def order_form(request):
    form = OrderForm()
    if request.method ==  "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect((reverse("home")))
    context={
        "form":form
    }
    return render (request,"project/order_form.html",context)
@login_required(login_url="login")
@admin_only
def update_order(request,id):
    obj = get_object_or_404(Order,id=id)
    form = OrderForm(instance=obj)
    context ={
        "form":form
    }
    if request.method == "POST":
        form = OrderForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect((reverse("customers")))
    return render(request,"project/order_form.html",context)
@login_required(login_url="login")
@admin_only
def delete_order(request,id):
    order = get_object_or_404(Order,id=id)
    if request.method == "POST":
        order.delete()
        return redirect(reverse("home"))
    context = {
        "order" : order
    }
    return render(request,"project/delete_order.html",context)
@login_required(login_url="login")
@admin_only
def create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    contex = {
        "form": form
    }
    return render(request,"project/customer_form.html",contex)
@login_required(login_url="login")
def update_customer(request,id):
    obj = get_object_or_404(Customer,id=id)
    form = CustomerForm(instance=obj)
    context ={
        "form":form
    }
    if request.method == "POST":
        form = CustomerForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect((reverse("home")))
    return render(request,"project/customer_form.html",context)
@login_required(login_url="login")
def delete_customer(request,id):
    customer = get_object_or_404(Customer,id=id)
    if request.method == "POST":
        customer.delete()
        return redirect(reverse("home"))
    context = {
        "customer" : customer
    }
    return render(request,"project/delete_customer.html",context)
@login_required(login_url="login")

def customer_order(request,id):
    orderformset= inlineformset_factory(Customer,Order,fields=("product","status"),extra=10)
    customer = Customer.objects.get(id = id)
    #form = OrderForm(initial={"customer":customer})
    form = orderformset(instance = customer)
    context ={
        "form":form
    }
    if request.method == "POST":
        form = orderformset(request.POST , instance = customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect((reverse("home")))
    return render(request,"project/customer_order.html",context)


@login_required(login_url="login")

def user(request):
    orders = request.user.customer.order_set.all()
    totol_orders = orders.count()
    dilivered = orders.filter(status="Dilivered").count()
    pending = orders.filter(status="Pending").count()
    contex={'orders' : orders,
            "totol_orders":totol_orders,
            "dilivered":dilivered,
            "pending":pending}
    return render(request,"project/user.html",contex)


def settings(request):
    user  = request.user
    form = CustomerForm(instance = user.customer)
    if request.method == "POST":
        form = CustomerForm(request.POST ,instance = user.customer)
        if form.is_valid():
            form.save()
            return redirect('user')
    context={
        "form":form,
        "user":user

    }
    return render(request,'project/settings.html',context)