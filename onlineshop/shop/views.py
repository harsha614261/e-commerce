from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from .models import upload,Cart,MyOrder,queries
import razorpay
from datetime import datetime
# Create your views here.
app_name='shop'
def home(request):
    return render(request,'main1.html')
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=="POST":
        uname=request.POST['uname']
        pass1=request.POST['password']
        user=auth.authenticate(username=uname,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('account')
        else:
            return render(request,'login.html')
def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        fname=request.POST['Firstname']
        lname=request.POST['Lastname']
        email=request.POST['E-mail']
        uname=fname+lname
        pass1=request.POST['fpassword']
        pass2=request.POST['spassword']
        if pass1==pass2:
            user=User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=lname,)
            user.save()
            return redirect('login')
def product(request):
    x=upload.objects.all()
    return render(request,'prod.html',{'uploads':x})
def account(request):
    if request.user.is_authenticated:
        y=upload.objects.all()
        uname=request.user.username
        return render(request,'account.html',{'uploads':y,'uname':uname})
    else:
        return render(request,'login.html')
def GetDetails(request,slug):
    t=upload.objects.get(pk=slug)
    context = {
        'getdata' : t
    }
    return render(request,'ProductData.html', context)
def BuyNow(request,slug):
    if request.user.is_authenticated:
        getpay=upload.objects.all()
        z=[]
        for t in getpay:
            z.append(t.Cname)
        if slug in z:
            return success(request,slug)
        elif slug=="account":
            return account(request)
        elif slug=="logout":
            return logout(request)
        elif slug=="order":
            return order(request)
        elif slug=="cart":
            return Mycart(request)
        for t in getpay:
            if int(t.id)==int(slug):
                getpays=t
        content={
            'getdata':getpays
        }
        s=(getpays.Cost)*100
        DATA = {
            "amount": getpays.Cost,
            "currency": "INR",
            "notes": {
            "key1": getpays.CInstructor,
            "key2": getpays.Cname,
            "cost":s,
            "key3":getpays.id,
            "key4":getpays.img.url,
            "key5":request.user.username,
            "key6":request.user.email,
            }
        }
        client= razorpay.Client(auth=("rzp_test_TYhQ1HZvFCtOrJ", "SoCES1fyPtE9ANzyjNEJV2U0"))
        x=client.order.create(data=DATA)
        return render(request,'address.html',{'x':x})
    else:
        return render(request,'login.html')
def AddToCart(request,slug):
    if request.user.is_authenticated:
        t=upload.objects.get(pk=slug)
        w=Cart.objects.all()
        s=[]
        for o in w:
            s.append(int(o.uid))
        if int(slug) not in s:
            x=Cart(uid=t.id,img=t.img,Cname=t.Cname,CInstructor=t.CInstructor,Cduration=t.Cduration,Ctopics=t.Ctopics,Accessibility=t.Accessibility,Cost=t.Cost)
            x.save()
            return HttpResponse("Added succesfully")
        else:
            return HttpResponse("Already Added")
    return redirect('login')
def success(request,slug):
    a=slug
    c=upload.objects.all()
    for e in c:
        if e.Cname==a:
            b=e.id

    x='Preparing for Dispatch'
    s=MyOrder(uname=request.user.username,mail=request.user.email,pid=b,status=x)
    s.save()
    return render(request,'success.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def order(request):
    z=MyOrder.objects.all()
    a=upload.objects.all()
    st=[]
    for t in z:
        orders=[]
        if t.uname==request.user.username and t.mail==request.user.email:
            #orders.append(t.pid)
            for e in a:
                if e.id==t.pid:
                    orders.append(e)
                    orders.append(t.status)
            st.append(orders)
    return render(request,'order.html',{'x':st})
def Mycart(request):
    e=Cart.objects.all()
    return render(request,'cart.html',{'uploads':e})
def SendQuery(request):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['email']
        Number=request.POST['number']
        Message=request.POST['message']
        w=queries(Name=Name,Email=Email,Number=Number,Message=Message)
        w.save()
        return redirect('/')
def owner(request):
    show_orders = MyOrder.objects.all()
    print(request.method)
    if request.method=="POST":
        username=request.POST['uname']
        email=request.POST['mail']
        prodid=request.POST['pid']
        cstatus=request.POST['status']
        for o in show_orders:
            a=str(datetime.now())
            if o.uname==username and o.mail==email and str(o.pid)==prodid:
                o.status+="--------"+a+"  "+cstatus
                o.save()
                return HttpResponse("Status Updated Successfully")
        return("Invalid data")
    products_details=upload.objects.all()
    return render(request,'adminpage.html',{'show_orders':show_orders,'products_details':products_details})
