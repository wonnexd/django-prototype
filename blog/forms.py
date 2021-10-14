from django import forms
from django.core.mail import message

class ContactForm(forms.Form):
	subject = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'style': 'width: 1000px',
			'placeholder' :'Worum geht es?',
			}
	))
	from_email = forms.CharField(widget=forms.EmailInput(
		attrs={
			'class': 'form-control',
			'style': 'width: 1000px',
			'placeholder' :'Emailadresse',
			}
	))
	message = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control',
			'style': 'width: 1000px',
			'placeholder' :'Ihre Nachricht hier',
			}
	))

# style django forms with bootstrap
# https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa