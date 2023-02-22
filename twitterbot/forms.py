from django import forms

class AccountForm(forms.Form):
    screen_name = forms.CharField(label="", max_length=300, widget=forms.TextInput(attrs={"placeholder": "@username"}))
