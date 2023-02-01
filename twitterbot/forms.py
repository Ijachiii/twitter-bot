from django import forms

class AccountForm(forms.Form):
    username = forms.CharField(label="@username", max_length=300)