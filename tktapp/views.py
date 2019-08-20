from django.shortcuts import render,redirect,render_to_response
from .models import Movies,Signup,Theatre,Booking,Post
from .forms import Moviesform,Signupform,Loginform,Moviesform,Theatreform,Bookingform
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def Sign(request):
    form = Signupform()
    if request.method =='POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()   
        return redirect(home)
    return render(request,'signup.html',{'form':form})

def login(request):
    form = Loginform()
    if request.method == 'POST':
        form= Loginform(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            log = Signup.objects.filter(email=email,password=password)
            if not log:
                return render(request,'login.html')
            else:
                return redirect(home)
        else:
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})

def movie(request):
    form = Moviesform()
    if request.method == 'POST':
        form = Moviesform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'movier.html',{"msg":"details successfully submited"})
    return render(request,'movier.html',{'form':form})

def mlist(request):
    mvlist = Movies.objects.all()
    return render(request,"mlist.html",{'form':mvlist})

def theatre(request):
    form = Theatreform()
    if request.method == 'POST':
        form = Theatreform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'theatre.html',{"msg":"details successfully submited"})
    return render(request,'theatre.html',{'form':form})

def thlist(request):
    tlist = Theatre.objects.all()
    return render(request,"thlist.html",{'form':tlist})

def booking(request):
    form = Bookingform()
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ticket)
    return render(request,'book.html',{'form':form})

def ticket(request):
    tick = Booking.objects.all()
    return render(request,"blist.html",{'form':tick})

def find(request):
    context = {}
    if request.method == 'POST':
        date_r = request.POST.get('date')
        time_r = request.POST.get('showtime')
        ticket_r = request.POST.get('ticketprice')
        theatre_r = request.POST.get('theatre')
        book_list = Booking.objects.filter(date=date_r, showtime=time_r, ticketprice=ticket_r)
        if book_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context["error"] = "Sorry no ticket availiable"
            return render(request, 'myapp/findbus.html', context)
    else:
        return render(request, 'myapp/findbus.html')

def seatl(request):
    return render(request,'seat.html')

def layout(request):
    return render(request,'layout.html')

def location(request):
    return render(request,'success.html')



# def createpost(request):
#         if request.method == 'POST':
#             if request.POST.get('date') and request.POST.get('movie') and request.POST.get('theatre')and request.POST.get('showtime') and request.POST.get('ticketprice') and request.POST.get('select_seat') and request.POST.get('name') and request.POST.get('mobile') :
#                 post=Post()
#                 post.date= request.POST.get('date')
#                 post.movie= request.POST.get('movie')
#                 post.theatre= request.POST.get('theatre')
#                 post.showtime= request.POST.get('showtime')
#                 post.ticketprice= request.POST.get('ticketprice')
#                 post.select_seat= request.POST.get('select_seat')
#                 post.name= request.POST.get('name')
#                 post.mobile= request.POST.get('mobile')
#                 post.save()
                
#                 return render(request, 'book.html')  

#         else:
#                 return render(request,'book.html')


# ['date','movie','theatre','showtime','ticketprice','select_seat','name','mobile']