from django.shortcuts import render
from django.http import HttpResponseRedirect
from bday_reminder.models import Patient
from django.core.mail import send_mail
from django.conf import settings
from datetime import date

# Create your views here.

def profile(request):
	if request.POST:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		phone = request.POST['phone']
		birthday = request.POST['birthday']
		p = Patient(first_name=first_name, last_name=last_name, email=email, phone=phone, birthday=birthday)
		p.save()
		return HttpResponseRedirect('/bday_reminder/profile')
	else:
		args = {}
		args['patients'] = Patient.objects.all()
		return render(request, 'bday_reminder/profile.html', args)

def send(request):

	bdays = Patient.objects.all().filter(birthday__month=date.today().month,birthday__day=date.today().day)
	patients = Patient.objects.all().filter(birthday__month=date.today().month,birthday__day=date.today().day,sent=False)
	subject = 'Happy Birthday'
	message = 'Wishing you a Happy Birthday from DrChrono!'
	sender = settings.EMAIL_HOST_USER

	for patient in patients:
		p = Patient.objects.get(first_name=patient.first_name, last_name=patient.last_name, birthday__month=date.today().month, birthday__day=date.today().day, sent=False)
		p.sent = True
		p.save()
		send_mail(subject, message, sender, [patient.email], fail_silently=False)

	args = {}
	if patients:
		args['message'] = 'Birthday Reminder Sent!'
	elif not bdays:
		args['message'] = 'No birthdays today!'
	else:
		args['message'] = 'You have already sent the birthday reminders today!'

	return render(request, 'bday_reminder/send.html', args)



