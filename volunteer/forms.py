from django import forms


class VolunteerForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
