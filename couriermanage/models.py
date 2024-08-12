from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


class Courier(models.Model):
	STATUS = (
        ('Pending','Pending'),
        ('Approved','Approved'),
		('Completed','Completed'),
    )

	tracking_id = models.CharField(max_length=255, null=True, unique=True)
	sender_name = models.CharField(max_length=255, null=True)
	sender_email = models.CharField(max_length=200,null=True)
	reciever_name = models.CharField(max_length=250, blank=True, null=True)
	reciever_email = models.EmailField(blank=True,null=True)
	origin = models.CharField(max_length=200, blank=True, null=True)
	destination = models.CharField(max_length=300, blank=True, null=True)
	description = models.CharField(blank=True, null=True, max_length=500)
	weight = models.CharField(blank=True, null=True, max_length=255)
	collection_date = models.DateTimeField(blank=True,  null=True)
	delivery_date = models.DateTimeField(blank=True, null=True)
	status = models.CharField(max_length=20, choices=STATUS, default='Pending',null=True)
	list_date = models.DateTimeField(default=timezone.datetime.now, blank = True, null=True)

	def get_absolute_url(self):
		return reverse("couriermanage:listing",args=[self.reference])

	def __str__(self):
		return self.tracking_id
	
	# def save(self):
	# 	if self.id:
	# 		old = Courier.objects.get(pk=self.id)
	# 		if old.status == 'ON' and self.sent == False:
	# 			user  = self.reciever_name
	# 			id = self.tracking_id
	# 			mail_subject = 'Shippment Notification'
                
	# 			message = render_to_string('box/shippment.html', {
    #                 'user' : user,
    #                 'id':id,
    #                 })
	# 			to_email = self.reciever_email
	# 			send_email = EmailMessage(mail_subject, message, to=[to_email])
	# 			send_email.content_subtype = "html"
	# 			send_email.send()
				
	# 			self.sent = True
	# 			old.save()
	# 	super(Courier, self).save()

class ShippingHistroy(models.Model):
	parcel = models.OneToOneField(Courier, on_delete=models.CASCADE)
	current_location = models.CharField(max_length=255, null=True, blank=False)
	current_status = models.CharField(max_length=255, null=True, blank=False)
	details = models.TextField(null=True, blank=True)
	date = models.DateTimeField(default=timezone.datetime.now, blank = True, null=True)

	def __str__(self):
		return  self.current_location

	def packacke_date(self):
         return self.date.strftime('%B %d %Y')

class Contact(models.Model):
	first_name = models.CharField(max_length=250,null=True)
	last_name = models.CharField(max_length=250,null=True)
	email = models.CharField(max_length=250,null=True)
	message_subject = models.CharField(max_length=200,null=True)
	message = models.CharField(max_length=500,null=True)
	date_added = models.DateTimeField(auto_now_add=True,null=True)
	
	def __str__(self):
	    return self.email
	
class Quote(models.Model):
	name = models.CharField(max_length=250,null=True)
	email = models.CharField(max_length=250,null=True)
	departure = models.CharField(max_length=200,null=True)
	arrival = models.CharField(max_length=500,null=True)
	cargo_description = models.TextField(max_length=1000,null=True)
	transportation_method = models.CharField(max_length=500,null=True)
	date_added = models.DateTimeField(auto_now_add=True,null=True)
	
	def __str__(self):
	    return self.name + ' ' + self.email