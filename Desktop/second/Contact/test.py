import psycopg2

import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=second user=postgres password=killer999")
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)",
        row
    )
conn.commit()

--------------------------------------------------------------------------------

data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="│"):
	    	_, created = Contact.objects.update_or_create(
	            first_name=column[0],
	            last_name=column[1],
	            email=column[2],
	            message=column[3]
	    	)
	context = {}
	return render(request, template, context)


	-----------------------------------------------------------------------
conn = psycopg2.connect("host=localhost dbname=second user=postgres password=killer999")
	cur = conn.cursor()
	csv_file = request.FILES['file']
	data_set = csv_file.read().decode('UTF-8')
	#next(data_set) # Skip the header row.
	for row in data_set:
			cur.execute(
				"INSERT INTO Contact VALUES (%s, %s, %s, %s, %s)",
						row
						    )
	conn.commit()
	if not csv_file.name.endswith('.csv'):
			message.error(request, 'This is not a csv file')
-----------------------------------------------------------------------------------


import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import ContactForm
from django.db import models
from django.contrib.postgres.fields import IntegerRangeField
import psycopg2
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
	# data_set = csv_file.read().decode('UTF-8')
	#conn = psycopg2.connect("host=localhost dbname=second user=postgres password=killer999")
	#cur = conn.cursor()
	elif request.method=='POST':
		conts=models.Contacts(
    		first_name = "Josh",
    		last_name = "Man",
    		email = "jm@gmail.com",
    		message = "hello data"
    		)
		conts.save()
		prompt["file_upload"]="the file is uploaded successfully."
		return render(request, template, prompt)
		# data_set='test.csv'
		# with open('test.csv', 'r') as f:
		#     reader = csv.reader(f)
		#     next(reader) # Skip the header row.
		#     for row in reader:

		#         cur.execute(
	#         "INSERT INTO Contact_contact VALUES (%s, %s, %s, %s)",
	#         row
	#     )
	# conn.commit()

--------------------------------------------------------------------------------
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

	if request.method=='POST':			
		data_set = pd.read_csv(csv_file).encoding='utf8'
		io_string = io.StringIO(data_set)
		next(io_string) # Skip the header row.
		for column in csv.reader(io_string, delimiter=',', quotechar="│"):
			conts=models.Contacts(data_set)
			conts.save()
		prompt["file_upload"]="the file is uploaded successfully."
		return render(request, template, prompt)

		========================================================================================

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

	if request.method=='POST':			
		data_set = pd.read_csv(csv_file,encoding='utf8')
		
		conts=models.Contacts(data_set)
		conts.save()
		prompt["file_upload"]="the file is uploaded successfully."
		return render(request, template, prompt)

		=====================================================================================

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

	if request.method=='POST':			
		data_set = pd.read_csv(csv_file,encoding='utf8')
		first_name= (data_set['first_name']),
		last_name = (data_set['last_name']),
		email = (data_set['email']),
		message = (data_set['message'])
conts=models.Contacts('id','first_name' ,'last_name' ,'email','message')
conts.save()
		