from django import forms

class AccountForm(forms.Form):
    username = forms.CharField(label="", max_length=300, widget=forms.TextInput(attrs={"placeholder": "@username"}))
