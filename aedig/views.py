from django.shortcuts import render
from django.http import HttpResponse
import json
import smtplib


def index(request):
	return render(request, 'index.html', {})


def message(request):
	if request.method == 'POST':
		msg = request.POST.get('msg')
		formData= request.POST.get('formData')
		data = json.loads(formData)
		name, subject, email, message = '', '', '', ''

		name = data[1]['value']
		email = data[2]['value']
		subject = data[3]['value']
		message = data[4]['value']

		infos = 'Nom: ' + name + '\nemail: ' + email + '\nSujet: ' + subject + '\nMessage: ' + message
		template = 'Salut Aedig! Nouveau Message:  \n ' + infos

		#Code for the email Sender... Lolllllz

		server = smtplib.SMTP('smtp.gmail.com', 25)
		server.connect("smtp.gmail.com",587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login('ralphrezososyal@gmail.com', "mariage090197")
		server.sendmail('ralphrezososyal@gmail.com', 'rallralph.haver@gmail.com', template)
		server.quit()

	return HttpResponse('Votre Message a ete envoyé avec Succes !!!')