import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import ContactForm
from django.db import models
from django.contrib.postgres.fields import IntegerRangeField
import pandas as pd
from . import models

def Contact(request):
	template = "Contact.html"

	if request.method =="POST":
	    form = ContactForm(request.POST)

	    if form.is_valid():
	    	form.save()

	else:
		form =ContactForm()

	context = {
	     'form':form,
	}
	return render(request,template,context)


@permission_required('admin.can_add_log_entry')

def Contact_upload(request):
	template = "Contact_upload.html"

	prompt = {
		'order': 'Order of the CSV should be first_name, last_name, email, message',
			}
			  
	if request.method =="GET":
		return render(request, template, prompt)
	    
	csv_file = request.FILES['file']
	
	csv_file = csv_file[1:,:]
	if request.method=='POST':			
		data_set = pd.read_csv(csv_file,encoding='utf8')
		
		conts=models.Contacts(data_set)
		conts.save()
		prompt["file_upload"]="the file is uploaded successfully."
		return render(request, template, prompt)