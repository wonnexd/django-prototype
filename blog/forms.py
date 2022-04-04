from django import forms
from blog.models import Choice
from django.forms import ModelForm, Textarea


class ContactForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "width: 100%",
            }
        )
    )
    from_email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "style": "width: 100%",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "style": "width: 100%",
            }
        )
    )
    captcha = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Please fill in 1",
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
