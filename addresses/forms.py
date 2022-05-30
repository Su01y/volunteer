from django import forms


class TaskForm(forms.Form):
    taskname = forms.CharField()
    organization = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
    required_quantity = forms.IntegerField()
    available_quantity = forms.IntegerField()