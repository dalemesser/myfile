from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('',views.home , name = "home"),
    path("products",views.products , name = "products"),
    path("<id>/customers",views.customer , name = "customer"),
    path("orderform",views.order_form , name = "createorder"),
    path("<id>/updateorder",views.update_order,name = "updateorder"),
    path("<id>/deleteorder",views.delete_order , name = "deleteorder"),
    path("customerform",views.create_customer , name = "createcustomer"),
    path("<id>/updatecustomer",views.update_customer,name = "updatecustomer"),
    path("<id>/deletecustomer",views.delete_customer , name = "deletecustomer"),
    path("<id>/customerorder",views.customer_order , name= "customerorder"),
    path("register",views.register,name="register"),
    path("login",views.login,name = "login"),
    path("logout",views.logout_view,name = "logout"),
    path('user',views.user ,name= 'user'),
    path("account",views.settings,name='account'),
    path("reset_password",auth_view.PasswordResetView.as_view(),name ="reset_password"),
    path("reset_password_sent",auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_view.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("reset_password_complete",auth_view.PasswordResetCompleteView.as_view(),name = "password_reset_complete")
]