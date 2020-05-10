from django.shortcuts import render, redirect
from django.http import HttpResponse
from homepage.models import ContactModel
from django.contrib import messages
from django.urls import reverse
import smtplib
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage


def homepage(request):
	if request.method == 'POST':
		name = request.POST.get("name", '')
		email = request.POST.get("email", '')
		subject = request.POST.get('subject', '')
		message = request.POST.get("message", '')
		contact = ContactModel(name=name, email=email, subject=subject, message=message)

		send_mail(
    'Thanks for the message',
    'Dear {},\nThis is to notify that your message is recevived. You will soon receive the email from Varun.\n\nThank you\n\nBot!'.format(name),
    settings.EMAIL_HOST_USER,[str(email)],fail_silently=False,)

		contact.save()

		
		messages.info(request, 'Your message is sucessfully delivered')

		return render(request, 'homepage/index.html', {})

	
	return render(request, 'homepage/index.html')



