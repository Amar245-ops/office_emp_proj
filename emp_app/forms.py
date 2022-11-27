from django import forms


class AddUserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    salary = forms.IntegerField()
    bonus = forms.IntegerField()
    phone = forms.IntegerField()
    role = forms.CharField(max_length=100)
    dept = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    hire_date = forms.DateInput()