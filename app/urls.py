from django.urls import path
from app import views
from django.contrib.auth import views as authview
from .forms import LoginForm,PassChangeForm,SetNewPassForm


urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),


    path('cart/', views.addtocart, name='addtocart'),
    path('showcart/', views.showcart, name='showcart'),


    path('removecartitem/', views.removecartitem),
    path('pluscart/', views.pluscart),
    path('minuscart/', views.minuscart),


    path('buy/', views.buy_now, name='buy-now'),
    path('orders/', views.orders, name='orders'),


    path('accounts/profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),

    # path('changepassword/', authview.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=PassChangeForm), name='changepassword'),
    path('changepassword/', views.changepassword, name='changepassword'),


    path('password-reset/', views.MyPassResetView.as_view(), name='passwordreset'),
    path('passresetdone/', authview.PasswordResetDoneView.as_view(template_name='app/passresetdone.html'), name='password_reset_done'),
    path('password-reset-link/<uidb64>/<token>/', authview.PasswordResetConfirmView.as_view(template_name='app/passresetconf.html',form_class=SetNewPassForm), name='password_reset_confirm'),
    path('passresetcomp/', authview.PasswordResetCompleteView.as_view(template_name='app/passresetcompleted.html'), name='password_reset_complete'),


    path('mobile/<slug:brnd>', views.mobile, name='mobile'),
    path('mobile/', views.mobile, name='mobile'),

    path('products/<str:category>', views.otherproducts, name='otherproducts'),
    path('products/', views.otherproducts, name='products'),
    path('product-detail/<int:id>', views.product_detail, name='product-detail'),

    # path('login/', views.Login.as_view(), name='login'),
    path('logout/', authview.LogoutView.as_view(next_page="home"), name='logout'),
    path('accounts/login/', authview.LoginView.as_view(redirect_authenticated_user ='/accounts/profile/',authentication_form=LoginForm,template_name = "app/login.html"), name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
]
