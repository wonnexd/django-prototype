from django import forms
from django.core.mail import message

class ContactForm(forms.Form):

	subject = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control' 
		}
	))

    from_email = forms.CharField(widget=forms.EmailInput(
		attrs={
			'class': 'form-control' 
		}
	))

	message = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control' 
		}
	))
