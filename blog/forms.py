from django import forms
from blog.models import Choice
from django.forms import ModelForm, SelectMultiple, Textarea


class ContactForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "width: 100%",
                "placeholder": "Worum geht es?",
            }
        )
    )
    from_email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "style": "width: 100%",
                "placeholder": "Emailadresse",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "style": "width: 100%",
                "placeholder": "Ihre Nachricht hier",
            }
        )
    )
    captcha = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Bitte 1 eintragen",
            }
        )
    )


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ("choice_text",)


widgets = {
    "choice_text": Textarea(attrs={"cols": 80, "rows": 20}),
}
