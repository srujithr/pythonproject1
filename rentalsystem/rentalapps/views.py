from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from .models import customusers
from datetime import datetime
from .models import Car,customusers
from .models import Booking
# Create your views here.


# ///////////////////// main index pages /////////////////////////
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, "service.html")

def car(request):
    return render(request, "car.html")

def contact(request):
    return render(request, "contact.html")

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['password']
        location = request.POST['location']
        company_name = request.POST['company_name']
        user = customusers.objects.create_user(username=username,first_name=first_name,last_name=last_name,user_type=0,email=email,address=address,company_name=company_name,
                                              phone=phone,password=password,location=location)
        user.save()
        # return redirect()
        return redirect(user_login)
    else:
        return render(request, 'register.html')


def company_register(request):
    if request.method == 'POST':
        company_name = request.POST['companyname']
        username = request.POST['username']
        company_address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        location = request.POST['location']
        password = request.POST['password']
        data = customusers.objects.create_user(company_name=company_name,address=company_address,location=location,user_type=1,phone=phone,username=username,
                                               email=email,password=password)
        data.save()
        return HttpResponse("company register successful")
    else:

        return render(request,'branch.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin_user = authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return redirect('admin:index')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 1:# company has logined
                return redirect(user_page)
            elif user.user_type == 0:# coutsomuser has has logined
                return redirect(userindex)
        else:
            return render(request, 'login.html',)

    return render(request, 'login.html')  

# ///////////////////// main index pages  end /////////////////////////







# ///////////////////// company  pages /////////////////////////




def cmpnyindex(request):
    return render(request, 'company/companyindex.html')


def user_page(request):
    return render(request, 'company/companyindex.html')

def bookings(request):
    return render(request, 'company/booking.html')



def add_car(request):
    user = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        name = request.POST['name']
        car_model = request.POST['car_model']
        price = request.POST['price']
        image = request.FILES['image']
        details = request.POST['details']
        new_car = Car.objects.create(company_id=user,name=name, car_model=car_model, price=price, details=details,image=image)
        new_car.save()
        # return HttpResponse('Car added successfully')
        return redirect(view_car)
    else:
        return render(request, 'company/addcar.html',)
    

def edit_car(request,id):
    user = customusers.objects.get(id=request.user.id)
    data = Car.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        car_model = request.POST['car_model']
        price = request.POST['price']
        details = request.POST['details']
        data = Car.objects.update(name=name, car_model=car_model,details=details,price=price)
        return redirect(view_car)
    else:
        return render(request,'company/edit.html',{'data':data})
    
def update_company(request):
    user = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        company_name = request.POST['company_name']
        address = request.POST['company_address']
        location = request.POST['location']
        data = customusers.objects.update(company_name=company_name,
            address=address,
            location=location
    )
        return HttpResponse('Update successful')
    else:

        return render(request, 'company/update.html')

def view_car(request):           
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.filter(company_id=user.id)
    print(data)
    return render(request, 'company/carview.html', {'data': data})








   










def view_requests(request):
    user = customusers.objects.get(id=request.user.id)
    print(user)
    datas = Car.objects.filter(company_id=user.id)
    print(datas)
    all_bookings = Booking.objects.filter(car__in=datas)
    return render(request, 'company/review.html',{'all_bookings': all_bookings})

def delete(request,id):
    user = customusers.objects.get(id=request.user.id)
    user = Car.objects.filter(id=id)

    user.delete()
    return redirect(view_car)


# ///////////////////// company  pages end /////////////////////////














# ///////////////////// user pages start /////////////////////////

def user_requests(request):
    user = customusers.objects.get(id=request.user.id)
    all_bookings = Booking.objects.filter(user=user)
    return render(request, 'user/viewrequest.html',{'all_bookings': all_bookings})

def abouts(request):
    return render(request, 'user/abouts.html')

def contacts(request):
    return render(request, 'user/contacts.html')

def userindex(request):
    return render(request, 'user/userindex.html')

def services(request):

    return render(request, 'user/services.html')






def details(request):
    return render(request, 'user/detail.html')


def cars(request):           
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.all()
    print(data)
    return render(request, 'user/cars.html', {'data': data})




def booking(requset):
    if requset.method == 'POST':
        user = requset.POST['user']
        no_of_days = requset.POST['no_of_days']
        day = requset.POST['day']
        Total_cost = requset.POST['Total_cost']
        booking_date = requset.POST[' booking_date']
        status = requset.POST['status']
        Bookings = Booking.objects.create(user=user,no_of_days=no_of_days,day=day,Total_cost=Total_cost,booking_date=booking_date,status='pending')

        Bookings.save()
        return HttpResponse('Booking successful')
    else:
        return render(requset, 'user/booking.html')


def company_review(request):
    data = customusers.objects.filter()
    return render(request, 'user/company_history.html',{'data':data})


def profile(request):
    data = customusers.objects.get(id=request.user.id)
    return render(request, 'user/profile.html', {'data': data})

def edit_profile(request,id):
    users = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        company_name = request.POST['company_name']
        data = customusers.objects.update(first_name=first_name,last_name=last_name,email=email,
                            address=address,company_name=company_name)
        return redirect(view_users)
    else:
        return render(request, 'user/editprofile.html',{'users':users})


def view_users(request):
    data = customusers.objects.get(id=request.user.id)
    print(data.first_name)
    return render(request, 'user/userview.html', {'data': data})

def car_request(request, id):
    user = customusers.objects.get(id=request.user.id)
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        no_of_days = int(request.POST['no_of_day'])
        day = request.POST['day']
        num = no_of_days * car.price

        booking_request = Booking.objects.create(
            user=user,
            car=car,
            no_of_days=no_of_days,
            day=day,
            Total_cost=num,
        )                                                                     
        booking_request.save()

        return redirect(user_requests)
    
    else:
        return render(request,'user/request.html',{'car': car})



def cart(request,id):
    if request.method == 'GET':
        car = Car.objects.get(id=id)
        return render(request,'user/cart.html',{'car':car})


def car_search(request):
    if request.method == "POST":
        car_name = request.POST['car_name']
        data = Car.objects.filter(name=car_name)
        return render(request, 'user/cars.html', {'data': data})
    else:
        return render(request, 'user/cars.html')




def statusrequest(request,id):
    datas = Booking.objects.get(id=id)
    if request.method == 'POST':
        booking = request.POST['booking']
        if booking == 'accepted':
            datas.status = 'approved'
        elif booking == 'reject':
            datas.status = 'rejected'
        
        elif booking == 'complete':
            datas.status = 'completed'
        datas.save()
    return redirect(view_requests)



        
        




def user_history(request):
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.filter(company_id=user.id)
    print(data)
    data = customusers.objects.all()
    return render(request, '    user/user_history.html',{'datta':data})



# ///////////////////// company  pages end /////////////////////////




# ///////////////////// logout /////////////////////////

def userlogout(request):
    auth.logout(request)
    return redirect(index)



# ///////////////////// logout end /////////////////////////


def update_status(request, id):
    booking = Booking.objects.get(id=id)

    if request.method == 'POST':
        booking.status = 'paid'
        
        booking.save()

        return redirect(user_requests)
    else:
        return render(request, 'user/payment.html', {'a': booking})
    



def history(request):
    user = customusers.objects.get(id=request.user.id)
    data = Car.objects.filter(company_id = user.id)
    datas = Booking.objects.filter(status='paid',car__in=data)
    return render(request, 'company/history.html', {'all_bookings': datas})


def userhistory(request):
    datas = Booking.objects.all()
    return render(request, 'user/userhistory.html', {'all_bookings': datas})

def review_add(request,id):
    data = Booking.objects.get(id=id)
    print(data)
    if request.method == 'POST':
        review  = request.POST['review']
        print(review)
    
        Rating = request.POST['rating']
        print(Rating)
        data.review = review
        data.Rating = Rating
    
        data.save()
        print(data.review)
        print(data.Rating)
        return HttpResponse('added')
    else:
        return render(request,'viewrequest.html',{'datas':data})
    

def booking_review(request):
    datas = Booking.objects.all() 
    return render(request, 'user/cars.html', {'datas': datas})