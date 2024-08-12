from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import Courier
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import *
# import folium
# import geocoder

def home(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		departure = request.POST['departure']
		arrival = request.POST['arrival']
		cargo_description = request.POST['cargo_description']
		transportation_method = request.POST['transportation_method']
		data = Quote.objects.create(name=name,email=email,departure=departure,arrival=arrival,cargo_description=cargo_description,transportation_method=transportation_method)
		data.save();
		messages.success(request, 'Your quote has been submitted ','')
		return render(request, 'box/index.html', {})
	else:
		return render(request, 'box/index.html', {})

def search(request):
	query = request.GET.get('q')
	if query is None:
		couriers = Courier.objects.none()
		histroys = ShippingHistroy.objects.none()
		m = None
		t = None
	else:
		couriers = Courier.objects.filter(tracking_id__icontains=query)
		t = ShippingHistroy.objects.filter(parcel=couriers.first())
    
		
	
	return render(request,'box/search.html', {'couriers':couriers,'histroys':t,})



# def listing(request, id=None):

#     listing = get_object_or_404(Courier, id=id)
    
#     # transaction = get_object_or_404(Transaction, parcel=listing.id)
	
#     t = ShippingHistroy.objects.all().filter(parcel=listing.id)
    
#     adr = ShippingHistroy.objects.get()
#     location = geocoder.osm(adr.current_location)
#     lat = location.lat
#     lng = location.lng
#     country = location.country
#     m = folium.Map(location=[lat, lng], zoom_start=2)
#     folium.Marker([lat, lng], tooltip='Click for more',
#                   popup=country).add_to(m)
#     m = m._repr_html_()
#     context = {
#         'listing':listing,
# 		'transactions':t,
# 		'm': m,
# 		}

#     return render(request, 'box/listing.html', context)

def about(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		departure = request.POST['departure']
		arrival = request.POST['arrival']
		cargo_description = request.POST['cargo_description']
		transportation_method = request.POST['transportation_method']
		data = Quote.objects.create(name=name,email=email,departure=departure,arrival=arrival,cargo_description=cargo_description,transportation_method=transportation_method)
		data.save();
		messages.success(request, 'Your quote has been submitted ','')
		return render(request, 'box/index.html', {})
	else:
		return render(request, 'box/about.html', {})

def services(request):
	return render(request, 'box/service.html', {})

def sea_freight(request):
	return render(request, 'box/sea-freight.html', {})

def air_freight(request):
	return render(request, 'box/air-freight.html', {})

def land_freight(request):
	return render(request, 'box/land-freight.html', {})

def warehouse(request):
	return render(request, 'box/warehouse.html', {})

def custom_clearance(request):
	return render(request, 'box/custom-clearance.html', {})

def contact(request):
	if request.method == "POST":
		massage_firstname = request.POST['firstname'] 
		massage_lastname = massage_firstname
		massage_email = request.POST['email']
		massage_subject = request.POST['massage_subject']
		massage = request.POST['message']
            #send mai
            
		contact = Contact.objects.create(first_name=massage_firstname,last_name=massage_lastname,email=massage_email,message_subject=massage_subject,message=massage)
		contact.save();
		messages.success(request, 'Your massage has been submitted ','')
		# send_mail(
		# 	massage_firstname + ''+ massage_lastname +' sent you an enquiry '+ massage_email + ' '+ massage_subject,
		# 	massage,
		# 	'arizonatymothy@gmail.com',
		# 	['arizonatymothy@gmail.com',],
		# 	fail_silently=False
		# 	)
		# messages.success(request, 'Your email has been sent ','alert alert-success alert-dismissible')
		return render(request, 'box/contact.html', {})
	else:
		return render(request, 'box/contact.html', {})


def track(request):
	return render(request, 'box/tracking.html', {})




def sign_in(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	else:
			
		if request.method == 'POST':
			username = request.POST['Username']
			password = request.POST['Password']

			user = auth.authenticate(username=username, password=password)

			if user is not None:
				auth.login(request,user)
				messages.success(request, 'Login Success')
				return HttpResponseRedirect(reverse('main')) 
			else:
				messages.error(request, 'Invalid credentials')
				return redirect('/login')
		else:
			return render(request, 'log/login.html',{})
		


def register(request):
	if request.user.is_authenticated:
		return redirect('home')
    
   
	else:

		if request.method == 'POST':
			first_name = request.POST['firstname']
			last_name = request.POST['lastname']
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password1']
			password2 = request.POST['password2']
		

			if password==password2:
				if User.objects.filter(email=email).exists():
					messages.warning(request, 'Email Taken')
					return redirect('/register')
				elif User.objects.filter(username=username).exists():
					messages.warning(request, 'Username Taken')
					return redirect('/register')
				else:
					user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name,last_name=last_name,)
					user.save();
					messages.success(request, 'You are now registered and can log in')
					print('user created')
					return redirect('/login')

			else:
				messages.warning(request, 'Password Not Matching')
				return HttpResponseRedirect('/register')
			return HttpResponseRedirect('/register')

		else:
			return render(request, 'log/register.html', {})


  
	


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
