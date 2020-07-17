from django import forms

from .models import Contacts

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contacts
		fields = ('first_name','last_name','email','message')
	
		