from django import forms
from .models import TwitterAccountChecked

class TwitterAccountCheckedForm(forms.ModelForm):
    class Meta:
        model = TwitterAccountChecked
        fields = ["screen_name"]
        widgets = {"screen_name": forms.TextInput(attrs={"placeholder": "@username"})} 

#class AccountForm(forms.Form):
#    screen_name = forms.CharField(label="", max_length=300, widget=forms.TextInput(attrs={"placeholder": "@username"}))
