from django.shortcuts import render,redirect
from . forms import UsrForm,OrForm,UsupForm,SelForm,PAccptForm,SelUpForm,PaymentForm
from . models import User,Order,Sell,Payment
from Carpentry import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def register(request):
	if request.method == "POST" :
		g = UsrForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/lgi')
	g = UsrForm()
	return render(request,'html/register.html',{'t':g})

def contact(request):
	if request.method == "POST":
		e=request.POST['em']
		s=request.POST['sb']
		d=request.POST['des']
		y=settings.EMAIL_HOST_USER
		z=send_mail(s,d,y,[e])
		if z==1:
			messages.success(request,"Mail Sent Successfully")
			return redirect('/con')
		else:
			return HttpResponse("Not send")
	return render(request,'html/contact.html')

def order(request):
	w = User.objects.get(id=request.user.id)
	if request.method == "POST":
		t = OrForm(request.POST,request.FILES)
		y = UsupForm(request.POST,instance=w)
		if t.is_valid() and y.is_valid():
			k = t.save(commit=False)
			k.cd_id = request.user.id
			w.has_order = 1
			w.save()
			y.save()
			k.save()
			return redirect('/')
	t = OrForm()
	y = UsupForm(instance=w)
	return render(request,'html/order.html',{'q':y,'r':t})

def sell(request):
	if request.method == "POST" :
		g5 = SelForm(request.POST,request.FILES)
		if g5.is_valid():
			g5.save()
			return redirect('/sell')
	g5 = SelForm()
	w1 = Sell.objects.all()
	return render(request,'html/sellprdcts.html',{'ff':g5,'fg':w1})

def orderlist(request):
	ac = User.objects.filter(role_type='1')
	data1=[]
	for nj in ac:
		ac_object=nj
		ol_object=None
		ol_object=Order.objects.filter(cd_id=nj.id)
		for jn in ol_object:
			ol_object=jn
		data1.append({'olis':ol_object,'cust':ac_object})
	return render(request,'html/orderlist.html',{'data2':data1})

def ProdAcc(request,id):
	pp = Order.objects.get(id=id)
	if request.method == "POST":
		p2=PAccptForm(request.POST,instance=pp)
		if p2.is_valid():
			cd_id = '2'
			pp.o_stat='Accepted'
			pp.save()
			p2.save()
			return redirect('/olist')
	p2 = PAccptForm(instance=pp)
	return render(request,'html/prodacc.html',{'p1':p2})

def orderstatus(request):
	ad = Order.objects.filter(cd_id=request.user.id)
	return render(request,'html/orderstatus.html',{'a3':ad})

def Categ(request):
	return render(request,'html/categ.html')

def chair(request):
	ch = Sell.objects.filter(f_name='Chair')
	return render(request,'html/chairs.html',{'c1':ch})

def door(request):
	dr = Sell.objects.filter(f_name='Door')
	return render(request,'html/doors.html',{'d1':dr})

def bed(request):
	bd = Sell.objects.filter(f_name='Bed')
	return render(request,'html/beds.html',{'b1':bd})

def sofas(request):
	sf = Sell.objects.filter(f_name='Sofa')
	return render(request,'html/sofas.html',{'s1':sf})

def dinning(request):
	tb = Sell.objects.filter(f_name='Table')
	return render(request,'html/dinning.html',{'t1':tb})

def chdetView(request,id):
	w = Sell.objects.get(prdct_id=id)
	return render(request,'html/chairdetail.html',{'w1':w})
def accept(request,id):
	k=Order.objects.get(id=id)
	k.o_stat='Accepted'
	k.save()
	return redirect('pa')

def reject(request,id):
	k=Order.objects.get(id=id)
	k.o_stat='Rejected'
	k.save()
	return redirect('olist')

def cancel(request,id):
	k=Order.objects.get(id=id)
	k.o_stat='Cancelled'
	k.save()
	return redirect('ostat')

def selstat(request,id):
	k=Order.objects.get(prdct_id=id)
	k.o_stat='Sold'
	k.save()
	return redirect('ostat')

def selUpd(request,id):
	sp = Sell.objects.get(prdct_id=id)
	if request.method == 'POST':
		s1 = SelUpForm(request.POST,instance=sp)
		if s1.is_valid():
			sp.save()
			s1.save()
			return redirect('/sell')
	s1=SelUpForm(instance=sp)
	return render(request,'html/selupdate.html',{'s3':s1})

def seldel(request,id):
	sq = Sell.objects.get(prdct_id=id)
	sq.delete()
	return redirect('/sell')

def selcancel(request,id):
	dd = Order.objects.get(id=id)
	Sell.objects.create(prdct_id=dd.id, im1=dd.img1, im2=dd.img2, dim=dd.dimensions, wd_type=dd.wood_type, f_name=dd.furniture_name, c_price=dd.wood_price + dd.manfac_price, o_price=0.00)
	dd.delete()
	return redirect('/olist') 



def dodetView(request,id):
	t = Sell.objects.get(prdct_id=id)
	return render(request,'html/drdetails.html',{'t1':t})
def bddetView(request,id):
	k = Sell.objects.get(prdct_id=id)
	return render(request,'html/bddetail.html',{'k1':k})
def sodetView(request,id):
	m = Sell.objects.get(prdct_id=id)
	return render(request,'html/sodetail.html',{'m1':m})
def dndetView(request,id):
	z = Sell.objects.get(prdct_id=id)
	return render(request,'html/dndetail.html',{'z1':z})


def payment(request, category, id):
    print(f"Category {category} and Id {id}")
    usDet=User.objects.get(id=request.user.id)
    selldet=Sell.objects.get(prdct_id=id)
    if request.method == 'POST':
    	pform=PaymentForm(request.POST)
    	formData=pform.save(commit=False)
    	formData.cc_id==request.user.id
    	formData.save()
    	selldet.s_stat='Sold'
    	selldet.save()
    	return render(request, 'html/Pa.html')
    pform=PaymentForm()
    return render(request, 'html/payment.html',{'v2':usDet,'y2':selldet,'zz':pform})

def opayment(request, id):
    if id == 999:
        k5 = PaymentForm(request.POST)
        uu = k5.save(commit=False)  # Corrected variable name from `k4` to `k5`
        uu.cc_id = request.user.id
        uu.save()
        return redirect('/tqpage')
    
    k5 = PaymentForm()
    y4 = Order.objects.get(id=id)
    abc = y4.furniture_name
    abd = y4.wood_price + y4.manfac_price
    v4 = User.objects.get(id=request.user.id)

    return render(request, 'html/ordpay.html', {'y5': abc, 'y6': abd, 'v5': v4, 'k6': k5})


def psu_payment(request):
	return render(request,'html/Pa.html')
