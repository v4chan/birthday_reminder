from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime, requests, pytz
from bday_reminder.models import Patient, User_Credential
# from django.contrib.auth.models import User

def login(request):
	return render(request, 'login.html', {})

def auth(request):

	code = request.GET.get('code')

	# getting access and refresh token
	response = requests.post('https://drchrono.com/o/token/', data={
	    'code': code,
	    'grant_type': 'authorization_code',
	    'redirect_uri': 'http://127.0.0.1:8000/authenticate/',
	    'client_id': 'Ur5LSA3czS3sXFuiUH22vNTeIP7LCIa7llFxuAYr',
	    'client_secret': 'BKXg7hp2NGZgjNbqKrzGogZKViFCBKmvhOa2XLKo9fsglMQ3HwnOO2HANyimWgbntRKRhYFq6iUGjpMbmHUqLWEUK1Sm6ofKdTpWEmYVH7wIquzGLZB4g9renDMBfF3Q',
	})
	response.raise_for_status()
	data = response.json()

	# Save these in your database associated with the user
	access_token = data['access_token']
	refresh_token = data['refresh_token']
	expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])
	User_Credential.objects.all().delete()
	uc = User_Credential(access_token=access_token, refresh_token=refresh_token, expiry_time=expires_timestamp)
	uc.save()
	# response = requests.get('https://drchrono.com/api/users/current', headers={
	# 	'Authorization': 'Bearer %s' % access_token,
	# })
	# response.raise_for_status()
	# data = response.json()
	headers = {
	    'Authorization': 'Bearer %s' % access_token,
	}

	patients = []
	patients_url = 'https://drchrono.com/api/patients'
	while patients_url:
	    data = requests.get(patients_url, headers=headers).json()
	    patients.extend(data['results'])
	    patients_url = data['next'] # A JSON null on the last page

	#clear patient info in database
	Patient.objects.all().delete()

	#store patient info in database
	for patient in patients:
		first_name = patient['first_name']
		last_name = patient['last_name']
		email = patient['email']
		phone = patient['cell_phone']
		birthday = patient['date_of_birth']
		sent = False
		p = Patient(first_name=first_name, last_name=last_name, email=email, phone=phone, birthday=birthday, sent=sent)
		p.save()

	return HttpResponseRedirect('/bday_reminder/profile')
