from django.shortcuts import render,redirect
from .models import Cart,CustomerInfo,Product,OrderPlaced
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.http import HttpResponseRedirect,JsonResponse
from .forms import ProfileForm,RegisterationForm,PassChangeForm,PassResetForm
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.db.models import Q
# from .forms import LoginForm 


class HomeView(View): 
 def get(self,request):
  mobs = Product.objects.filter(category='MOB')
  wchs = Product.objects.filter(category='WCH')
  ebds = Product.objects.filter(category='EB')
  laps = Product.objects.filter(category='LAP')
  if request.user.is_authenticated:
    cartcount = Cart.objects.filter(user=request.user).count()
  else:
    cartcount = ""
  return render(request,'app/home.html',{'mobs':mobs,'wchs':wchs,'ebds':ebds,'laps':laps,'cartcount':cartcount})


def product_detail(request,id):
 product_detail = Product.objects.get(pk=id)
 cartcount=""
 if request.user.is_authenticated:
  cartcount = Cart.objects.filter(user=request.user).count()
 return render(request, 'app/productdetail.html',{'proddetail':product_detail,'cartcount':cartcount})


def addtocart(request):
  user = request.user
  proddata = Product.objects.get(pk=request.GET['prod_id'])
  sv=Cart(user=user,product=proddata)
  sv.save()
  return HttpResponseRedirect('/showcart/')


def showcart(request):
  cartdata=Cart.objects.filter(user=request.user)
  cartcount=Cart.objects.filter(user=request.user).count()
  cart_product_list=[items for items in cartdata if items.user == request.user]
  shipping = 70.00
  tempamount= 0.0
  amount = 0.0
  totalamount=0.0
  if cart_product_list:
    for item in cart_product_list:
      tempamount = item.quantity*item.product.discounted_price
      amount += tempamount
      totalamount=amount+shipping
  return render(request,'app/addtocart.html',{'cartdata':cartdata,'cartcount':cartcount,'totalamount':totalamount,'amount':amount})

def pluscart(request):
  a = request.GET.get('prodid')
  b = Cart.objects.get(Q(product=a) & Q(user=request.user))
  b.quantity+=1
  b.save()
  cartdata=Cart.objects.filter(user=request.user)
  cart_product_list=[items for items in cartdata if items.user == request.user]
  shipping = 70.00
  tempamount= 0.0
  amount = 0.0
  totalamount=0.0
  if cart_product_list:
    for item in cart_product_list:
      tempamount = item.quantity*item.product.discounted_price
      amount += tempamount
      totalamount=amount+shipping
    data={'quantity':b.quantity,'amount':amount,'totalamount':totalamount}
  return JsonResponse(data)


def minuscart(request):
  a = request.GET['prodid']
  b = Cart.objects.get(Q(user=request.user) & Q(product=a))
  b.quantity-=1
  b.save()
  cartdata=Cart.objects.filter(user=request.user)
  cart_product_list=[items for items in cartdata if items.user == request.user]
  shipping = 70.00
  tempamount= 0.0
  amount = 0.0
  totalamount=0.0
  if cart_product_list:
    for item in cart_product_list:
      tempamount = item.quantity*item.product.discounted_price
      amount += tempamount
      totalamount=amount+shipping
    data={'quantity':b.quantity,'amount':amount,'totalamount':totalamount}
  return JsonResponse(data)


def removecartitem(request):
  cartid = request.GET['cartid']
  a = Cart.objects.get(pk=cartid)
  b = Cart.objects.filter(user=request.user)
  a.delete()
  data={'status':'deleted'}
  return JsonResponse(data)



def buy_now(request):
 return render(request, 'app/buynow.html')


def profile(request):
 if request.user.is_authenticated:
  cartcount = Cart.objects.filter(user=request.user).count()
  if request.method=="POST":
    form=ProfileForm(request.POST)
    if form.is_valid():
      name=form.cleaned_data['name']
      zipcode=form.cleaned_data['zipcode']
      state=form.cleaned_data['state']
      city=form.cleaned_data['city']
      locality=form.cleaned_data['locality']
      sv= CustomerInfo(locality=locality,name=name,zipcode=zipcode,state=state,city=city,user=request.user)
      sv.save()
      messages.success(request,'profile sucessfully created')
  else:
    form=ProfileForm
  return render(request, 'app/profile.html',{'profileform':form,'cartcount':cartcount})


def address(request):
 if request.user.is_authenticated:
  cartcount = Cart.objects.filter(user=request.user).count()
  userdata=CustomerInfo.objects.filter(user=request.user)
  return render(request, 'app/address.html',{'data':userdata,'cartcount':cartcount})


def orders(request):
 cartcount = Cart.objects.filter(user=request.user).count()
 a= OrderPlaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html',{'cartcount':cartcount,'ordereditems':a})


def changepassword(request):
  if request.user.is_authenticated:
    cartcount = Cart.objects.filter(user=request.user).count()
    if request.method =='POST':
      form=PassChangeForm(user= request.user , data= request.POST)
      if form.is_valid():
        form.save()
        messages.success(request,'Password Changed Successfully')
    else:
      form = PassChangeForm(user = request.user)
    return render(request, 'app/changepassword.html',{'pcform':form,'cartcount':cartcount})
  

class MyPassResetView(PasswordResetView):
  template_name='app/forgetpass.html'
  form_class=PassResetForm


def mobile(request,brnd=None):
  cartcount=""
  if request.user.is_authenticated:
    cartcount = Cart.objects.filter(user=request.user).count()
  if brnd=='redmi' or brnd=='samsung' or brnd=='apple':
    mobile = Product.objects.filter(brand=brnd , category='MOB')
  elif brnd == 'below':
    mobile = Product.objects.filter(category='MOB').filter(MRP__lt=30000)
  elif brnd == 'above':
    mobile = Product.objects.filter(category='MOB').filter(MRP__gt=50000)
  else:
    mobile = Product.objects.filter(category='MOB').order_by('product_name')
  return render(request, 'app/mobile.html', {'mobs':mobile,'cartcount':cartcount})


# class Login(View):
#  def get(self,request):
#   form=LoginForm()
#   return render(request,'app/login.html',{'form':form})

#  def post(self,request):
#   form=LoginForm(request.POST)
#   if form.is_authenticated():
#    return HttpResponseRedirect()
#   else:
#    return render(request,'app/login.html',{'form':form})



def customerregistration(request):
  if request.method=='POST':
    form = RegisterationForm(request.POST)
    if form.is_valid():
     form.save()
     form = RegisterationForm()
     messages.success(request,'registeration successful')
  else:
    form = RegisterationForm()
  return render(request, 'app/customerregistration.html',{'regform':form})


def checkout(request):
  if request.user.is_authenticated:
    usercartitem=Cart.objects.filter(user=request.user)
    orderedprod=OrderPlaced.objects.filter(user=request.user)
    address = CustomerInfo.objects.filter(user=request.user)
    cart_product_list=[items for items in usercartitem if items.user == request.user]
    shipping = 70.00
    tempamount= 0.0
    amount = 0.0
    totalamount=0.0
    if cart_product_list:
      for item in cart_product_list:
        tempamount = item.quantity*item.product.discounted_price
        amount += tempamount
        totalamount=amount+shipping
  return render(request,'app/checkout.html',{'address':address,'cartitems':usercartitem,'totalamount':totalamount})



# <--This Function Is Made By Me To Fetch All Products Data-->
def otherproducts(request,category=None):
  cartcount=""
  if request.user.is_authenticated:
    cartcount = Cart.objects.filter(user=request.user).count()
  data = Product.objects.filter(category=category)
  return render(request,'app/otherproducts.html',{'data':data,'cartcount':cartcount})

def paymentdone(request):
  user = request.user
  addid = request.GET.get('custid')
  address = CustomerInfo.objects.get(pk=addid)
  items = Cart.objects.filter(user=user)
  for i in items:
    OrderPlaced(user=user,customer_info=address,product=i.product,quantity=i.quantity).save()
    i.delete()
  return redirect("orders")