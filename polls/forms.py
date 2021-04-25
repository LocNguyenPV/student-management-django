from django import forms
# import GeeksModel from models.py
from .models import Student

# creating a form
# class InputForm(forms.Form):
#     registration_number = forms.CharField(max_length=11)
#     name = forms.CharField(max_length=200)
#     email = forms.EmailField(max_length=200)
#     home_town = forms.CharField(max_length=200)
#     score = forms.IntegerField()
#     date_of_birth = forms.DateField()

# create a ModelForm
class InputForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = ('registration_number',
                    'name',
                    'email',
                    'home_town',
                    'score',
                    'date_of_birth'
                    )
